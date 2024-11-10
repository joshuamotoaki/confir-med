# ConfirMed

**Smarter and safer self-administration of medications**

<h1 align="center">
  <img src="apps/web/static/logo.png" alt="ConfirMed Logo" width="50%">
</h1>

## Overview

By Joshua Lau, Ansh Desai, Ella Myslo, and Joshua Cheuk.

ConfirMed is a comprehensive medication management platform that helps patients safely identify and track their medications while maintaining clear communication with healthcare providers. Using advanced machine learning for pill recognition and an intuitive user interface, ConfirMed makes medication management more reliable and stress-free.

## Repository Structure

The repository is a mono-repo containing the source code for the web application, API service, and mobile app.

```
confirMed/
├── app/
│   ├── web/        # SvelteKit web application
│   ├── api/        # Flask API with ML model
│   └── app/        # Expo React Native mobile app
```

## Applications

### Web Application (/app/web)

- Built with SvelteKit
- Styled using TailwindCSS and ShadCN-svelte
- Features:
  - Dashboard for healthcare providers
  - Patient medication tracking
  - Secure messaging system
  - Medication interaction warnings

### API Service (/app/api)

- Flask-based REST API
- Custom machine learning model for pill recognition
- Features:
  - Image processing pipeline
  - Drug identification
  - Interaction checking
  - Authentication and authorization

### Mobile App (/app/app)

- Built with Expo React Native
- Features:
  - Medication scanning
  - Schedule management
  - Reminder system
  - Direct communication with healthcare providers
  - Offline functionality

## Getting Started

### Prerequisites

- Node.js 18+
- Python 3.9+
- iOS 13+ or Android 9+

### Installation

1. Clone the repository:

```bash
git clone https://github.com/confirMed/confirMed.git
cd confirMed
```

2. Install web dependencies and run the development server:

```bash
cd app/web
npm install
npm run dev
```

3. Install API dependencies and run the API server:

```bash
cd ../api
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

4. Install mobile app dependencies and start the development server:

```bash
cd ../app
npm install
npx expo start
```

## Disclaimer

Note: This application is intended to assist with medication management but should not be used as the sole method of verification. Always consult healthcare providers and read medication labels carefully.

## License

This project is licensed under the BSD 3-Clause License - see the [LICENSE](LICENSE) file for details.
