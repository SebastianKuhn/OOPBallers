import argparse
import base64
import json
import sys


class GenerateGoogleVisionRequest(object):

    detection_types = []
    file_format_description = ""

    def __init__(self):
        self.detection_types = [
            'TYPE_UNSPECIFIED',
            'FACE_DETECTION',
            'LANDMARK_DETECTION',
            'LOGO_DETECTION',
            'LABEL_DETECTION',
            'TEXT_DETECTION',
            'SAFE_SEARCH_DETECTION',
        ]
        self.file_format_description = """ Each line in the input file must be of the form:
            file_path feature:max_results feature:max_results ....
        
            where 'file_path' is the path to the image file you'd like
            to annotate, 'feature' is a number from 1 to %s,
            corresponding to the feature to detect, and max_results is a
            number specifying the maximum number of those features to
            detect.
            
            The valid values - and their corresponding meanings - for
            'feature' are:
            
            %s""".strip() % (
                            len(self.detection_types) - 1,
                            # The numbered list of detection types
                            '\n    '.join(
                                # Don't present the 0th detection type ('UNSPECIFIED') as an option.
                                '%s: %s' % (i + 1, detection_type)
                                for i, detection_type in enumerate(self.detection_types[1:]))
                    )

    def translate_input_file(self, input_file, output_filename):

        """Translates the input file into a json output file.

            Args:
                input_file: a file object, containing lines of input to convert.
                output_filename: the name of the file to output the json to.
            """
        # Collect all requests into an array - one per line in the input file
        request_list = []
        for line in input_file:
            # The first value of a line is the image. The rest are features.
            image_filename, features = line.lstrip().split(' ', 1)

            # First, get the image data
            with open(image_filename, 'rb') as image_file:
                content_json_obj = {
                    'content': base64.b64encode(image_file.read()).decode('UTF-8')
                }

            # Then parse out all the features we want to compute on this image
            feature_json_obj = []
            for word in features.split(' '):
                feature, max_results = word.split(':', 1)
                feature_json_obj.append({
                    'type': self.get_detection_type(feature),
                    'maxResults': int(max_results),
                })

            # Now add it to the request
            request_list.append({
                'features': feature_json_obj,
                'image': content_json_obj,
            })

        # Write the object to a file, as json
        with open(output_filename, 'w') as output_file:
            json.dump({'requests': request_list}, output_file)

    def get_detection_type(self, detect_num):
        """Return the Vision API symbol corresponding to the given number."""
        detect_num = int(detect_num)
        if 0 < detect_num < len(self.detection_types):
            return self.detection_types[detect_num]
        else:
            return self.detection_types[0]

    @staticmethod
    def generate_visionrequest(self):
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter
        )
        parser.add_argument(
            '-i', dest='input_file', required=True,
            help='The input file to convert to json.\n' + self.file_format_description)
        parser.add_argument(
            '-o', dest='output_file', required=True,
            help='The name of the json file to output to.')
        args = parser.parse_args()
        try:
            with open(args.input_file, 'r') as input_file:
                self.translate_input_file(input_file, args.output_file)
        except ValueError as e:
            sys.exit('Invalid input file format.\n' + self.file_format_description)
