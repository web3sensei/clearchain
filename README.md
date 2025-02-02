<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ClearChain - Open Source LLM Vulnerability Scanner</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }

        h1, h2, h3 {
            color: #2c3e50;
        }

        h1 {
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }

        h2 {
            color: #2980b9;
            margin-top: 30px;
        }

        code {
            background-color: #f5f5f5;
            padding: 2px 5px;
            border-radius: 3px;
        }

        pre {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }

        .badges {
            margin: 20px 0;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .feature-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }

        .feature-card {
            padding: 15px;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }

        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #f8f9fa;
        }

        a {
            color: #3498db;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>ClearChain</h1>
    <p><strong>The open-source LLM Vulnerability Scanner</strong></p>

    <div class="badges">
        <img src="https://img.shields.io/github/contributors/yourusername/clearchain" alt="Contributors">
        <img src="https://img.shields.io/github/last-commit/yourusername/clearchain" alt="Last Commit">
        <img src="https://img.shields.io/pypi/dm/clearchain" alt="Downloads">
        <img src="https://img.shields.io/github/issues/yourusername/clearchain" alt="Issues">
        <img src="https://img.shields.io/github/license/yourusername/clearchain" alt="License">
    </div>

    <h2>Features</h2>
    <div class="feature-list">
        <div class="feature-card">
            <h3>🛠️ Customizable Rule Sets</h3>
            <p>Create agent-based attack configurations tailored to your needs</p>
        </div>
        <div class="feature-card">
            <h3>🧪 Comprehensive Fuzzing</h3>
            <p>Test any LLM implementation with extensive attack vectors</p>
        </div>
        <div class="feature-card">
            <h3>🌀 Multi-Modal Support</h3>
            <p>Test text, image, and audio processing systems</p>
        </div>
    </div>

    <h2>Installation</h2>
    <pre><code>pip install clearchain</code></pre>

    <h2>Quick Start</h2>
    <pre><code># Start the server
clearchain --port=8718 --host=0.0.0.0

# Run basic scan
clearchain ci</code></pre>

    <h2>CI/CD Integration</h2>
    <p>Sample GitHub Action workflow:</p>
    <pre><code>name: Security Scan
on: [push]
jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run ClearChain
        run: |
          pip install clearchain
          clearchain ci</code></pre>

    <h2>Documentation</h2>
    <p>Full documentation available at: <a href="https://clearchain.dev/docs">https://clearchain.dev/docs</a></p>

    <h2>Roadmap</h2>
    <table>
        <tr>
            <th>Feature</th>
            <th>Status</th>
            <th>ETA</th>
        </tr>
        <tr>
            <td>OWASP Top 10 Integration</td>
            <td>✅ Completed</td>
            <td>Q3 2024</td>
        </tr>
        <tr>
            <td>Adaptive Attacker LLM</td>
            <td>🔄 In Progress</td>
            <td>Q4 2024</td>
        </tr>
    </table>

    <h2>Contributing</h2>
    <ol>
        <li>Fork the repository</li>
        <li>Create your feature branch</li>
        <li>Commit your changes</li>
        <li>Push to the branch</li>
        <li>Open a Pull Request</li>
    </ol>

    <h2>License</h2>
    <p>Apache License 2.0 - See <a href="LICENSE">LICENSE</a> for details</p>
</body>
</html>
