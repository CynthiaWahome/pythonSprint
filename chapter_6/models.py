# designs []  -> completed models 

def print_models(unprinted_designs, completed_models=[]):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("-------Printing mode- ------", current_design)
        print("\n Printing complete --------")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    for model in completed_models:
        print(model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)

show_completed_models(completed_models)

print(unprinted_designs)

print(completed_models)
