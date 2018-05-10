"""
extract important vales from responses
"""

search_recipe = {

}





recipe_information = {
    "vegatarian" : response["body"]["vegetarian"],
    "aggregateLikes" : response["body"]["aggretageLikes"],
    "health_score" : response["body"]["healthScore"],
    "ingredients": [
        for ingredient in response["body"]["extendedIngredients"]:
            {
                "iid" : response["body"]["extendedIngredients"]["id"],
                "name" : response["body"]["extendedIngredients"]["name"],
                "meta" : response["body"]["extendedIngredients"]["metaInformation"],
                "amount" : response["body"]["extendedIngredients"]["measures"]["metric"]["amount"],
                "unit" : response["body"]["extendedIngredients"]["measures"]["metric"]["unitShort"]
            }]
}
