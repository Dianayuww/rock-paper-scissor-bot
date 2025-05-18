import random

# Global variable to store opponent history and transition dictionary
opponent_history = []
transition_table = {}

def update_transition_table(history):
    if len(history) < 2:
        return
    prev = history[-2]
    curr = history[-1]
    if prev not in transition_table:
        transition_table[prev] = {"R": 0, "P": 0, "S": 0}
    transition_table[prev][curr] += 1

def predict_next_move():
    if len(opponent_history) < 1:
        return random.choice(["R", "P", "S"])
    last = opponent_history[-1]
    if last in transition_table:
        predicted = max(transition_table[last], key=transition_table[last].get)
        return predicted
    else:
        return random.choice(["R", "P", "S"])

def counter_move(move):
    counters = {"R": "P", "P": "S", "S": "R"}
    return counters[move]

def player(prev_play, opponent_history=[]):
    import random
    counter_moves = {"R": "P", "P": "S", "S": "R"}

    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        # Awal-awal main acak atau selalu "R"
        return "R"

    # Ambil pola 3 langkah terakhir musuh
    last_pattern = "".join(opponent_history[-3:])

    # Hitung frekuensi setelah pola tertentu
    patterns = {}
    for i in range(len(opponent_history) - 3):
        pattern = "".join(opponent_history[i:i+3])
        next_move = opponent_history[i+3]
        if pattern not in patterns:
            patterns[pattern] = {"R":0, "P":0, "S":0}
        patterns[pattern][next_move] += 1

    # Prediksi langkah musuh selanjutnya
    if last_pattern in patterns:
        prediction = max(patterns[last_pattern], key=patterns[last_pattern].get)
        return counter_moves[prediction]
    else:
        return random.choice(["R", "P", "S"])
