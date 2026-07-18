# quick test of the rag engine
import sys
sys.path.insert(0, '.')

from rag_engine import DriveWiseRAG

engine = DriveWiseRAG()

print("\n" + "=" * 60)
print("DriveWise Quick Test")
print("=" * 60)

tests = [
    ("Hyundai", "Creta", "What is the mileage?"),
    ("Hyundai", "Creta", "How many airbags?"),
    ("Tata", "Nexon", "What is the safety rating?"),
    ("Maruti Suzuki", "Brezza", "What is the price?"),
    (None, None, "Which car has best ground clearance?"),
]

for brand, model, q in tests:
    result = engine.ask(q, brand, model)
    label = f"{brand} {model}" if brand else "All Cars"
    print(f"\n[{label}] Q: {q}")
    print(f"A: {result['answer'][:150]}...")
    print(f"Sources: {[s['section'] for s in result['sources']]}")
    print(f"Time: {result['response_time']}s")

print("\n--- Stats ---")
print(engine.get_query_stats())
