# Voice Cloning Model

## Introduction

Welcome to the Voice Cloning Model project! This repository contains code and resources for building a voice cloning model using PyTorch. While my initial attempt to complete this project was unsuccessful due to system limitations, I am excited to share the progress I have made and encourage others to contribute and finish the work.

### Features

- Voice cloning using PyTorch.
- Custom dataset handling.
- put your mp3 recordings in recordings folder
- Training script with batch processing.

## Getting Started

Follow these steps to get started with the project:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/heathbrew/Voice-Cloning-Model
   ```

2. Install the required dependencies. You can use the following command to install them:

   ```bash
   ./VoiceCloning2.ps1
   ```

3. Download your dataset and place it in the appropriate directory.

4. Modify the provided code to suit your dataset and model architecture.

## Usage

To use the code provided in this repository, follow these steps:

1. Customize the `SimpleTTSModel` class in the code to define your voice cloning model.

2. Prepare your dataset in the format required by the `CustomDataset` class.

3. Modify the training loop in the `train` function to match your specific training requirements.

4. Train your model using the `train` function and save the trained model weights.

5. You can then use the trained model for voice cloning by loading the saved model weights and calling `model.eval()`.

## Roadmap

This project is a work in progress. Here are some of the planned improvements and features:

- Integration with more advanced voice cloning techniques.
- Support for different audio and text formats.
- Enhanced model architecture for better voice quality.

## How to Contribute

I encourage you to contribute to this project and help it reach its full potential. Here's how you can get involved:

1. Fork the repository.
2. Create a new branch for your contributions:

   ```bash
   git checkout -b feature/your-feature
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Add your feature or fix"
   ```

4. Push your changes to your fork:

   ```bash
   git push origin feature/your-feature
   ```

5. Create a pull request to merge your changes into the main branch of this repository.


## Contact

If you have any questions, suggestions, or would like to collaborate on this project, please feel free to reach out to me:

- [Linkedin](https://www.linkedin.com/in/ayushman-pranav-20b49ba3/)
