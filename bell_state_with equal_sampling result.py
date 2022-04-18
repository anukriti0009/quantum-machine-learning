# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:34:54 2022

@author: anukriti

Bell State creation and Measurement using Qiskit and sampling equally on measurement of bell state
"""
import numpy as np
from qiskit import QuantumCircuit,execute,Aer
from qiskit.visualization import plot_histogram
#using aer qasm simulator
simulator = Aer.get_backend('qasm_simulator')

#create a quantum circuit acting on quantum register
circuit = QuantumCircuit(2,2)

#adding hadamard gate to the qubit 0 
circuit.h(0)

#adding a cnot gate on control qubit 0 and target qubit 1
circuit.cx(0,1)

#measuring the output and mapping the results of qubit 1 and 2 in classical reg 1 and 2

circuit.measure([0,1],[0,1])

#execute the circuit on qasm simulator
job = execute(circuit,simulator,shots = 1000)

#getting results form the job
result = job.result()

#returns counts
counts = result.get_counts(circuit)


print("total number of 00 and 11 are as follows:",counts)

print(circuit)

#a circuit with equal number of bell states





