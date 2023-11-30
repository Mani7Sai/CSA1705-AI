class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_valid_assignment(self, assignment, variable, color):
        for neighbor in self.constraints[variable]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        variable = [var for var in self.variables if var not in assignment][0]

        for color in self.domains[variable]:
            if self.is_valid_assignment(assignment, variable, color):
                assignment[variable] = color
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                del assignment[variable]

        return None

    def solve(self):
        assignment = self.backtrack({})
        return assignment


def main():
    # User Input
    variables = input("Enter the variables (comma-separated): ").split(',')
    domains = {var: input(f"Enter domain for {var} (space-separated colors): ").split() for var in variables}
    constraints = {}
    
    print("Enter the constraints. Enter 'done' when finished.")
    while True:
        constraint = input("Enter constraint (var1 var2): ").split()
        if constraint[0].lower() == 'done':
            break
        if constraint[0] not in constraints:
            constraints[constraint[0]] = []
        if constraint[1] not in constraints:
            constraints[constraint[1]] = []
        constraints[constraint[0]].append(constraint[1])
        constraints[constraint[1]].append(constraint[0])

    # CSP
    map_coloring_csp = MapColoringCSP(variables, domains, constraints)
    solution = map_coloring_csp.solve()

    # Display Result
    print("\nMap Coloring Result:")
    for variable, color in solution.items():
        print(f"{variable}: {color}")


if __name__ == "__main__":
    main()
