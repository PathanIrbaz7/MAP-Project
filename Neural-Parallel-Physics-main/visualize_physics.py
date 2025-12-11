"""
Physics Simulation Visualization & Comparison Graphs
Generates comprehensive visual comparisons of physics components
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Rectangle
import sys
import importlib.util

# Inject numpy into the ParallelPhysics module before importing
spec = importlib.util.spec_from_file_location("ParallelPhysics", 
    r"c:\Users\irbaz\Downloads\Neural-Parallel-Physics-main\Neural-Parallel-Physics-main\ParallelPhysics.py")
module = importlib.util.module_from_spec(spec)
module.np = np
sys.modules['ParallelPhysics'] = module
spec.loader.exec_module(module)

# Import classes
ConstantBalancer = module.ConstantBalancer
EnergyMassLink = module.EnergyMassLink
EnergyEvolution = module.EnergyEvolution
QuantumTransformation = module.QuantumTransformation
DynamicSurvival = module.DynamicSurvival
EnergyDispersionProblem = module.EnergyDispersionProblem
FormulaEngine = module.FormulaEngine
MassIncreaseSolution = module.MassIncreaseSolution
QuantumPhysicsImprovement = module.QuantumPhysicsImprovement


def generate_mass_balance_comparison():
    """Generate constant balancer comparison graph"""
    balancer = ConstantBalancer()
    
    mass_values = np.linspace(1, 100, 50)
    const_1 = np.array([balancer.balance(m, 1) for m in mass_values])
    const_2 = np.array([balancer.balance(m, 2) for m in mass_values])
    const_5 = np.array([balancer.balance(m, 5) for m in mass_values])
    
    return {
        'title': 'Mass Balance Comparison',
        'x_data': mass_values,
        'series': [
            {'label': 'const=1', 'data': const_1},
            {'label': 'const=2', 'data': const_2},
            {'label': 'const=5', 'data': const_5}
        ],
        'xlabel': 'Input Mass',
        'ylabel': 'Balanced Mass'
    }


def generate_energy_mass_correlation():
    """Generate energy-mass correlation comparison graph"""
    link = EnergyMassLink()
    
    energy_values = np.linspace(10, 500, 50)
    mass_5 = np.array([link.correlation(e, 5) for e in energy_values])
    mass_10 = np.array([link.correlation(e, 10) for e in energy_values])
    mass_20 = np.array([link.correlation(e, 20) for e in energy_values])
    
    return {
        'title': 'Energy-Mass Correlation',
        'x_data': energy_values,
        'series': [
            {'label': 'mass=5', 'data': mass_5},
            {'label': 'mass=10', 'data': mass_10},
            {'label': 'mass=20', 'data': mass_20}
        ],
        'xlabel': 'Energy',
        'ylabel': 'Correlation Value'
    }


def generate_energy_evolution():
    """Generate energy evolution over time"""
    evolution = module.EnergyEvolution()
    
    initial_energies = [50, 100, 200]
    time_steps = np.linspace(0, 20, 50)
    
    series = []
    for init_energy in initial_energies:
        evolved = np.array([evolution.update(init_energy, t) for t in time_steps])
        series.append({'label': f'Initial={init_energy}', 'data': evolved})
    
    return {
        'title': 'Energy Evolution Over Time',
        'x_data': time_steps,
        'series': series,
        'xlabel': 'Time Steps',
        'ylabel': 'Energy Level'
    }


def generate_dynamic_survival_comparison():
    """Generate dynamic survival comparison"""
    survival = DynamicSurvival()
    
    adaptability_values = np.linspace(0.1, 1.0, 50)
    needs_10 = np.array([survival.evaluate(10, a) for a in adaptability_values])
    needs_20 = np.array([survival.evaluate(20, a) for a in adaptability_values])
    needs_50 = np.array([survival.evaluate(50, a) for a in adaptability_values])
    
    return {
        'title': 'Dynamic Survival Evaluation',
        'x_data': adaptability_values,
        'series': [
            {'label': 'needs=10', 'data': needs_10},
            {'label': 'needs=20', 'data': needs_20},
            {'label': 'needs=50', 'data': needs_50}
        ],
        'xlabel': 'Adaptability',
        'ylabel': 'Survival Score'
    }


def generate_mass_increase_progression():
    """Generate mass increase over energy"""
    mass_inc = MassIncreaseSolution()
    
    energies = np.linspace(0, 500, 50)
    initial_masses = [5, 10, 20, 50]
    
    series = []
    for init_mass in initial_masses:
        new_masses = np.array([mass_inc.apply(e, init_mass) for e in energies])
        series.append({'label': f'Initial Mass={init_mass}', 'data': new_masses})
    
    return {
        'title': 'Mass Increase with Energy',
        'x_data': energies,
        'series': series,
        'xlabel': 'Energy Input',
        'ylabel': 'Final Mass'
    }


def generate_quantum_physics_evolution():
    """Generate full quantum physics system evolution"""
    class MockObject:
        def __init__(self):
            self.location = type('obj', (object,), {'x': 0, 'y': 0, 'z': 0})()
    
    obj = MockObject()
    physics = QuantumPhysicsImprovement(obj, mass=10.0, energy=50.0)
    
    frames = range(30)
    masses = []
    energies = []
    positions = []
    states_x = []
    
    for frame in frames:
        physics.update_physics(0.016)
        masses.append(physics.mass)
        energies.append(physics.energy)
        positions.append(obj.location.z)
        states_x.append(physics.state[0])
    
    return {
        'title': 'Quantum Physics System Evolution (30 Frames)',
        'x_data': list(frames),
        'series': [
            {'label': 'Mass', 'data': np.array(masses)},
            {'label': 'Energy', 'data': np.array(energies)},
            {'label': 'Position Z', 'data': np.array(positions) * 100},  # Scale for visibility
            {'label': 'State[0]', 'data': np.array(states_x) / 10}  # Scale for visibility
        ],
        'xlabel': 'Frame Number',
        'ylabel': 'Value (scaled)'
    }


def generate_energy_dispersion_comparison():
    """Generate energy dispersion patterns"""
    dispersion = EnergyDispersionProblem()
    
    energy_maps = [
        [100, 0, 0],
        [50, 50, 0],
        [60, 30, 10],
        [40, 40, 40]
    ]
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Energy Dispersion Patterns', fontsize=16, fontweight='bold')
    
    for idx, energy_map in enumerate(energy_maps):
        ax = axes[idx // 2, idx % 2]
        result = dispersion.solve(energy_map)
        
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
        ax.bar(['Component 1', 'Component 2', 'Component 3'], result, color=colors, alpha=0.7, edgecolor='black')
        ax.set_ylabel('Dispersed Energy Fraction')
        ax.set_title(f'Input: {energy_map}')
        ax.set_ylim([0, 1])
        ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    return fig


def create_comparison_visualizations():
    """Create all comparison graphs"""
    
    print("🎨 Generating Physics Simulation Visualization Graphs...\n")
    
    # Create figure with multiple subplots
    fig = plt.figure(figsize=(18, 12))
    gs = gridspec.GridSpec(3, 2, figure=fig, hspace=0.35, wspace=0.3)
    
    # 1. Mass Balance Comparison
    print("  [1/6] Generating Mass Balance Comparison...")
    data = generate_mass_balance_comparison()
    ax1 = fig.add_subplot(gs[0, 0])
    for series in data['series']:
        ax1.plot(data['x_data'], series['data'], label=series['label'], linewidth=2.5, marker='o', markersize=3)
    ax1.set_xlabel(data['xlabel'], fontsize=10)
    ax1.set_ylabel(data['ylabel'], fontsize=10)
    ax1.set_title(data['title'], fontsize=12, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Energy-Mass Correlation
    print("  [2/6] Generating Energy-Mass Correlation...")
    data = generate_energy_mass_correlation()
    ax2 = fig.add_subplot(gs[0, 1])
    for series in data['series']:
        ax2.plot(data['x_data'], series['data'], label=series['label'], linewidth=2.5, marker='s', markersize=3)
    ax2.set_xlabel(data['xlabel'], fontsize=10)
    ax2.set_ylabel(data['ylabel'], fontsize=10)
    ax2.set_title(data['title'], fontsize=12, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 3. Energy Evolution
    print("  [3/6] Generating Energy Evolution...")
    data = generate_energy_evolution()
    ax3 = fig.add_subplot(gs[1, 0])
    for series in data['series']:
        ax3.plot(data['x_data'], series['data'], label=series['label'], linewidth=2.5, marker='^', markersize=3)
    ax3.set_xlabel(data['xlabel'], fontsize=10)
    ax3.set_ylabel(data['ylabel'], fontsize=10)
    ax3.set_title(data['title'], fontsize=12, fontweight='bold')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # 4. Dynamic Survival
    print("  [4/6] Generating Dynamic Survival Comparison...")
    data = generate_dynamic_survival_comparison()
    ax4 = fig.add_subplot(gs[1, 1])
    for series in data['series']:
        ax4.plot(data['x_data'], series['data'], label=series['label'], linewidth=2.5, marker='D', markersize=3)
    ax4.set_xlabel(data['xlabel'], fontsize=10)
    ax4.set_ylabel(data['ylabel'], fontsize=10)
    ax4.set_title(data['title'], fontsize=12, fontweight='bold')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    # 5. Mass Increase Progression
    print("  [5/6] Generating Mass Increase Progression...")
    data = generate_mass_increase_progression()
    ax5 = fig.add_subplot(gs[2, 0])
    for series in data['series']:
        ax5.plot(data['x_data'], series['data'], label=series['label'], linewidth=2.5)
    ax5.set_xlabel(data['xlabel'], fontsize=10)
    ax5.set_ylabel(data['ylabel'], fontsize=10)
    ax5.set_title(data['title'], fontsize=12, fontweight='bold')
    ax5.legend()
    ax5.grid(True, alpha=0.3)
    
    # 6. Quantum Physics Evolution
    print("  [6/6] Generating Quantum Physics System Evolution...")
    data = generate_quantum_physics_evolution()
    ax6 = fig.add_subplot(gs[2, 1])
    for series in data['series']:
        ax6.plot(data['x_data'], series['data'], label=series['label'], linewidth=2.5, marker='*', markersize=6)
    ax6.set_xlabel(data['xlabel'], fontsize=10)
    ax6.set_ylabel(data['ylabel'], fontsize=10)
    ax6.set_title(data['title'], fontsize=12, fontweight='bold')
    ax6.legend()
    ax6.grid(True, alpha=0.3)
    
    # Main title
    fig.suptitle('🧠 Parallel Physics System - Comprehensive Comparison Graphs', 
                 fontsize=16, fontweight='bold', y=0.995)
    
    print("\n✅ Saving comparison graph...")
    output_path = r"c:\Users\irbaz\Downloads\Neural-Parallel-Physics-main\Neural-Parallel-Physics-main\physics_comparison_graphs.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"   Saved to: {output_path}")
    
    # Energy Dispersion Patterns
    print("\n  Generating Energy Dispersion Patterns...")
    fig_dispersion = generate_energy_dispersion_comparison()
    output_path2 = r"c:\Users\irbaz\Downloads\Neural-Parallel-Physics-main\Neural-Parallel-Physics-main\energy_dispersion_patterns.png"
    plt.savefig(output_path2, dpi=300, bbox_inches='tight')
    print(f"   Saved to: {output_path2}")
    
    plt.close('all')
    
    print("\n" + "="*70)
    print("✅ ALL GRAPHS GENERATED SUCCESSFULLY!")
    print("="*70)
    print("\n📊 Generated Visualizations:")
    print("   1. Mass Balance Comparison")
    print("   2. Energy-Mass Correlation")
    print("   3. Energy Evolution Over Time")
    print("   4. Dynamic Survival Evaluation")
    print("   5. Mass Increase with Energy")
    print("   6. Quantum Physics System Evolution")
    print("   7. Energy Dispersion Patterns")
    print("\n📁 Output Files:")
    print(f"   • physics_comparison_graphs.png")
    print(f"   • energy_dispersion_patterns.png")
    print("\n" + "="*70)


if __name__ == "__main__":
    try:
        create_comparison_visualizations()
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
