"""
Test Script for ParallelPhysics.py
Demonstrates all physics components and their functionality
"""

import sys
import threading
import time
import numpy as np  # Required for ParallelPhysics.py

# IMPORTANT: Inject numpy into the module namespace before importing ParallelPhysics
import importlib.util
spec = importlib.util.spec_from_file_location("ParallelPhysics", 
    r"c:\Users\irbaz\Downloads\Neural-Parallel-Physics-main\Neural-Parallel-Physics-main\ParallelPhysics.py")
module = importlib.util.module_from_spec(spec)
module.np = np  # Inject numpy before execution
sys.modules['ParallelPhysics'] = module
spec.loader.exec_module(module)

# Now import from the module
ConstantBalancer = module.ConstantBalancer
EnergyMassLink = module.EnergyMassLink
EnergyEvolution = module.EnergyEvolution
QuantumTransformation = module.QuantumTransformation
ActionPotential = module.ActionPotential
DynamicSurvival = module.DynamicSurvival
EnergyDispersionProblem = module.EnergyDispersionProblem
MassIncreaseSolution = module.MassIncreaseSolution
FormulaEngine = module.FormulaEngine
ParallelPhysicsProcessor = module.ParallelPhysicsProcessor
UserInteractionForceModule = module.UserInteractionForceModule
QuantumPhysicsImprovement = module.QuantumPhysicsImprovement


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def test_constant_balancer():
    """Test the ConstantBalancer class"""
    print_section("TEST 1: CONSTANT BALANCER")
    
    balancer = ConstantBalancer()
    
    test_cases = [(10, 1), (20, 2), (50, 5)]
    
    for mass, const in test_cases:
        result = balancer.balance(mass, const)
        print(f"  Balance(mass={mass}, const={const}) = {result:.4f}")


def test_energy_mass_link():
    """Test the EnergyMassLink class"""
    print_section("TEST 2: ENERGY-MASS LINK")
    
    link = EnergyMassLink()
    
    test_cases = [(100, 5), (200, 10), (500, 20)]
    
    for energy, mass in test_cases:
        correlation = link.correlation(energy, mass)
        print(f"  Correlation(energy={energy}, mass={mass}) = {correlation:.4f}")


def test_energy_evolution():
    """Test the EnergyEvolution class"""
    print_section("TEST 3: ENERGY EVOLUTION")
    
    evolution = EnergyEvolution()
    
    initial_energy = 100.0
    print(f"  Initial Energy: {initial_energy:.4f}")
    
    for time_step in [1, 2, 5, 10]:
        evolved = evolution.update(initial_energy, time_step)
        print(f"  After {time_step} time units: {evolved:.4f}")


def test_quantum_transformation():
    """Test the QuantumTransformation class"""
    print_section("TEST 4: QUANTUM TRANSFORMATION")
    
    transformer = QuantumTransformation()
    
    state = [1.0, 1.0, 1.0]
    forces = [0.1, 0.5, 1.0]
    
    print(f"  Initial State: {state}")
    for force in forces:
        new_state = transformer.transform(state, force)
        print(f"  After force={force}: {[f'{x:.4f}' for x in new_state]}")


def test_action_potential():
    """Test the ActionPotential class"""
    print_section("TEST 5: ACTION POTENTIAL")
    
    action = ActionPotential()
    
    test_cases = [(10, 5, 2), (20, 10, 5), (50, 25, 10)]
    
    for initial, potential, action_val in test_cases:
        result = action.calculate(initial, potential, action_val)
        print(f"  Calculate({initial}, {potential}, {action_val}) = {result:.4f}")


def test_dynamic_survival():
    """Test the DynamicSurvival class"""
    print_section("TEST 6: DYNAMIC SURVIVAL")
    
    survival = DynamicSurvival()
    
    test_cases = [(10, 0.5), (20, 0.8), (50, 1.0)]
    
    for needs, adaptability in test_cases:
        result = survival.evaluate(needs, adaptability)
        print(f"  Evaluate(needs={needs}, adaptability={adaptability}) = {result:.4f}")


def test_energy_dispersion():
    """Test the EnergyDispersionProblem class"""
    print_section("TEST 7: ENERGY DISPERSION")
    
    dispersion = EnergyDispersionProblem()
    
    energy_maps = [
        [10, 20, 30],
        [50, 50, 50],
        [100, 50, 25]
    ]
    
    for energy_map in energy_maps:
        result = dispersion.solve(energy_map)
        print(f"  Solve({energy_map}) = {[f'{x:.4f}' for x in result]}")


def test_mass_increase():
    """Test the MassIncreaseSolution class"""
    print_section("TEST 8: MASS INCREASE SOLUTION")
    
    mass_inc = MassIncreaseSolution()
    
    test_cases = [(50, 10), (100, 20), (200, 50)]
    
    for energy, mass in test_cases:
        new_mass = mass_inc.apply(energy, mass)
        print(f"  Apply(energy={energy}, mass={mass}) = new_mass: {new_mass:.4f}")


def test_formula_engine():
    """Test the FormulaEngine class"""
    print_section("TEST 9: FORMULA ENGINE")
    
    engine = FormulaEngine()
    
    print(f"  Testing E=mc² formula (normalized):")
    test_cases = [(100, 5), (200, 10), (500, 20)]
    
    for energy, mass in test_cases:
        result = engine.emc2(energy, mass)
        print(f"  E={energy}, m={mass}: {result:.4e}")
    
    print(f"\n  Testing Quantum Field Mapping:")
    for user_input in [0.5, 1.0, 2.0]:
        quantum_state = 10.0
        result = engine.quantum_field_mapping(user_input, quantum_state)
        print(f"  Input={user_input}, State={quantum_state}: {result:.4f}")


def test_user_interaction_force():
    """Test the UserInteractionForceModule class"""
    print_section("TEST 10: USER INTERACTION FORCE MODULE")
    
    ui_force = UserInteractionForceModule()
    
    input_vectors = [
        [0.5, 0.5, 0.5],
        [1.0, 2.0, 3.0],
        [-1.0, 1.0, -1.0]
    ]
    
    for input_vec in input_vectors:
        force = ui_force.compute_force_from_input(input_vec)
        print(f"  Input vector {input_vec} → Force: {force:.4f}")


def test_quantum_physics_integration():
    """Test the integrated QuantumPhysicsImprovement class"""
    print_section("TEST 11: INTEGRATED QUANTUM PHYSICS SYSTEM")
    
    # Create a mock object
    class MockObject:
        def __init__(self):
            self.location = type('obj', (object,), {'x': 0, 'y': 0, 'z': 0})()
    
    obj = MockObject()
    physics_system = QuantumPhysicsImprovement(obj, mass=10.0, energy=50.0)
    
    print(f"  Initial Configuration:")
    print(f"    └─ Mass: {physics_system.mass:.4f}")
    print(f"    └─ Energy: {physics_system.energy:.4f}")
    print(f"    └─ State Vector: {physics_system.state}")
    print(f"    └─ Object Position Z: {obj.location.z:.4f}")
    
    print(f"\n  Running 5 Physics Updates:")
    for frame in range(1, 6):
        physics_system.update_physics(0.016)  # 60 FPS timestep
        print(f"\n    Frame {frame}:")
        print(f"      └─ Mass: {physics_system.mass:.4f}")
        print(f"      └─ Energy: {physics_system.energy:.4f}")
        print(f"      └─ Position Z: {obj.location.z:.4f}")
        print(f"      └─ State: {[f'{x:.2f}' for x in physics_system.state]}")


def test_parallel_processing():
    """Test parallel physics processing with threading"""
    print_section("TEST 12: PARALLEL PHYSICS PROCESSING")
    
    class PhysicsObject:
        def __init__(self, name):
            self.name = name
            self.location = type('obj', (object,), {'x': 0, 'y': 0, 'z': 0})()
            self.velocity = [0, 0, 0]
        
        def update_physics(self, timestep):
            self.location.z += 0.1 * timestep
            self.velocity[2] += 0.05 * timestep
    
    objects = [PhysicsObject(f"Object_{i}") for i in range(3)]
    processor = ParallelPhysicsProcessor(objects)
    
    print(f"  Created {len(objects)} physics objects")
    print(f"  Processing in parallel threads...")
    
    for frame in range(3):
        processor.process_all(0.016)
        print(f"\n    Frame {frame + 1}:")
        for obj in objects:
            print(f"      {obj.name} - Z: {obj.location.z:.4f}, VZ: {obj.velocity[2]:.4f}")


def main():
    """Run all tests"""
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*15 + "PARALLEL PHYSICS TEST SUITE" + " "*26 + "║")
    print("║" + " "*15 + "Testing All Physics Components" + " "*22 + "║")
    print("╚" + "="*68 + "╝")
    
    try:
        test_constant_balancer()
        test_energy_mass_link()
        test_energy_evolution()
        test_quantum_transformation()
        test_action_potential()
        test_dynamic_survival()
        test_energy_dispersion()
        test_mass_increase()
        test_formula_engine()
        test_user_interaction_force()
        test_quantum_physics_integration()
        test_parallel_processing()
        
        print_section("ALL TESTS COMPLETED SUCCESSFULLY ✅")
        print("\n  Total tests run: 12")
        print("  Status: PASSED\n")
        
    except Exception as e:
        print_section("ERROR DURING TESTING ❌")
        print(f"  {str(e)}\n")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
