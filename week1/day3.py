exercises = 6
sets_per_exercise = 4
reps_per_set = 10
weight_per_rep_kg = 60 
session_duration_minutes = 45

total_sets = exercises * sets_per_exercise
total_reps = total_sets * reps_per_set
total_volume_kg = weight_per_rep_kg * total_reps
reps_per_minute = total_reps // session_duration_minutes
volume_exceeded = total_volume_kg > 10000

print("==== MOSES WORK OUT PLAN ====")
print(f"Total sets: {total_sets}")
print(f"Total reps: {total_reps}")
print(f"Total volume: {total_volume_kg} kg")
print(f"Reps per minute: {reps_per_minute} minutes")
print(f"Volume exceeded 10,000 kg target: {volume_exceeded}")