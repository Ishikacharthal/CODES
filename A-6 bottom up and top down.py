from dataclasses import dataclass
from typing import List


@dataclass
class Item:
    name: str
    profit: float
    weight: float

    @property
    def ratio(self) -> float:
        """Calculate profit gained per unit of weight."""
        return self.profit / self.weight


class FractionalKnapsack:
    def __init__(self, capacity: float, items: List[Item]):
        self.capacity = capacity
        self.items = items
        self.selected = []
        self.maximum_profit = 0.0

    def solve(self):
        """Solve the Fractional Knapsack using greedy ratio strategy."""

        # Highest profit/weight ratio comes first
        sorted_items = sorted(
            self.items,
            key=lambda item: item.ratio,
            reverse=True
        )

        remaining_capacity = self.capacity

        for item in sorted_items:

            if remaining_capacity <= 0:
                break

            # Take the complete item
            if item.weight <= remaining_capacity:

                fraction = 1.0
                taken_weight = item.weight
                earned_profit = item.profit

            # Take only the required fraction
            else:

                fraction = remaining_capacity / item.weight
                taken_weight = remaining_capacity
                earned_profit = item.profit * fraction

            self.selected.append(
                {
                    "name": item.name,
                    "weight": taken_weight,
                    "fraction": fraction,
                    "profit": earned_profit,
                    "ratio": item.ratio
                }
            )

            self.maximum_profit += earned_profit
            remaining_capacity -= taken_weight

        return self.maximum_profit

    def display_result(self):
        print("\n" + "=" * 55)
        print("        FRACTIONAL KNAPSACK - GREEDY METHOD")
        print("=" * 55)

        print(f"Knapsack Capacity : {self.capacity}")
        print(f"Maximum Profit    : {self.maximum_profit:.2f}")

        print("\nSelected Items:")
        print("-" * 55)

        for item in self.selected:
            print(
                f"{item['name']:8} | "
                f"Weight: {item['weight']:5.2f} | "
                f"Fraction: {item['fraction']:4.2f} | "
                f"Profit: {item['profit']:6.2f}"
            )

        print("-" * 55)


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

items = [
    Item("Object 1", 25, 18),
    Item("Object 2", 24, 15),
    Item("Object 3", 15, 10)
]

capacity = 20

knapsack = FractionalKnapsack(capacity, items)

knapsack.solve()
knapsack.display_result()