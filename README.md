# AWS DeepRacer “Robocop” Experiment Suite

This repository documents a series of reinforcement‑learning experiments aimed at training an autonomous **AWS DeepRacer** agent on the **2022 October Pro (clockwise) Forever Raceway** track.  
The project explores reward‑shaping strategies, hyper‑parameter tuning and curriculum learning to achieve consistent 100 % lap completion with competitive lap times.

---

## Project Goals

* Design a reward function that balances **centre‑line adherence**, **speed**, and **smooth steering**.  
* Iterate through multiple training runs to measure how incremental changes affect lap performance and stability.  
* Produce a champion model capable of sub‑45‑second laps with zero crashes and minimal resets.  
* Provide visual analytics — steering & speed distributions, reward heatmaps, trajectory traces — to explain agent behaviour.  

---

## Directory Layout

```
.
├── 01-robocop-model-01               # Baseline PPO run
├── 02-robocop-model-02               # Reward v1 (speed bias ↑)
├── 03-robocop-model-03               # Reward v2 (adaptive steering penalty)
├── 04-robocop-model-04               # Hyper‑parameter sweep
├── 05-robocop-model-03-clone-01      # Transfer‑learning test #1
├── 06-robocop-model-03-clone-02      # Transfer‑learning test #2
├── 06-robocop-model-03-clone-04      # Data‑augmentation test
├── 06-robocop-model-03-clone-05      # High‑speed curriculum
└── 06-robocop-model-03-clone-06-BEST # ⭐ Final champion model
```

Each model folder contains:

* `model/` – TensorFlow checkpoints exported by SageMaker  
* `logs/` – RoboMaker ROS logs  
* `metrics/` – JSON metrics for training & evaluation  
* `sim-trace/` – CSV traces with X/Y, steering, speed, reward …  
* `videos/` – MP4 replays of training iterations & evaluation laps  

---

## Key Results

| Metric | Champion Model |
|--------|----------------|
| Lap completion | 100 % |
| Best lap time | **41.89 s** |
| Resets / Off‑tracks | 3–4 per lap |
| Crashes | 0 |

Representative visuals are stored under `plots/`:

* **Action Distributions** – steering & throttle histograms  
* **Reward Heatmap** – average reward mapped over track coordinates  
* **Path Trace** – full trajectory overlay for evaluation laps  

---

## Demo
https://github.com/user-attachments/assets/022aac7b-cfbd-4a53-94ea-76b82bf0d39a


Heatmap
![image](https://github.com/user-attachments/assets/0c189c7a-ff64-42c8-b90b-8c6bdd50132c)



---

## License

All original code and analysis © 2025 — released under the MIT License.  
AWS DeepRacer binaries are subject to AWS terms of service.
