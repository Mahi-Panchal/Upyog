def waste_agent(label):

    actions = {

    "cardboard":"Recycle in cardboard recycling bin",

    "glass":"Dispose in glass recycling container",

    "metal":"Send to metal scrap recycling",

    "paper":"Place in paper recycling bin",

    "plastic":"Send to plastic recycling facility",

    "trash":"Dispose in landfill waste bin"
    }

    return actions[label]
