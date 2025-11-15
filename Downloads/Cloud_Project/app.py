from flask import Flask
app = Flask(__name__)

@app.route('/')
def portfolio():
    # All of your resume content is built into this HTML string.
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shivpoojan Tiwari - Portfolio</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
        .container {
            max-width: 900px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
        header {
            text-align: center;
            padding-bottom: 20px;
            border-bottom: 2px solid #eee;
        }
        header h1 {
            margin: 0;
            color: #2c3e50;
        }
        header p {
            font-size: 1.1em;
            color: #3498db;
            margin: 5px 0 10px;
        }
        .links a {
            margin: 0 10px;
            text-decoration: none;
            color: #3498db;
            font-weight: bold;
        }
        .section {
            margin-top: 30px;
        }
        .section h2 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 5px;
            display: inline-block;
        }
        .skills-list {
            list-style: none;
            padding: 0;
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        .skills-list li {
            background-color: #ecf0f1;
            color: #333;
            padding: 8px 15px;
            border-radius: 20px;
            font-size: 0.9em;
        }
        .project-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
        }
        .card {
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            transition: transform 0.2s;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .card h3 {
            margin-top: 0;
            color: #3498db;
        }
        .job {
            margin-bottom: 15px;
            padding-left: 15px;
            border-left: 3px solid #ecf0f1;
        }
        .job h3 {
            margin: 0;
        }
        .job p {
            margin: 5px 0 0;
            font-style: italic;
            color: #555;
        }
        footer {
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            color: #777;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>SHIVPOOJAN TIWARI</h1>
            <p>AI, Cybersecurity, and Data-Driven Solutions</p>
            <div class="links">
                <a href="mailto:mvmoraishivpujan12b@gmail.com">Email</a>
                <a href="#">LinkedIn</a>
                <a href="#">Personal Portfolio</a>
            </div>
        </header>

        <div class="section">
            <h2>About Me</h2>
            <p>To leverage my expertise in AI, Cybersecurity, and data-driven solutions to drive innovation and deliver impactful results in the tech industry, while continuously growing as a leader.</p>
        </div>

        <div class="section">
            <h2>Technical Skills</h2>
            <ul class="skills-list">
                <li>Java</li>
                <li>Python</li>
                <li>C</li>
                <li>C++</li>
                <li>HTML</li>
                <li>CSS</li>
                <li>JavaScript</li>
                <li>Bootstrap</li>
                <li>Cybersecurity</li>
            </ul>
        </div>

        <div class="section">
            <h2>Projects</h2>
            <div class="project-grid">
                <div class="card">
                    <h3>Disease Outbreak Prediction</h3>
                    <p>Utilized TensorFlow, Scikit-Learn, and other advanced machine learning frameworks to design and implement a robust disease outbreak prediction model.</p>
                </div>
                <div class="card">
                    <h3>Personal Bucket List</h3>
                    <p>Developed a user-friendly web application for managing personal bucket lists using modern front-end technologies such as HTML5, CSS3, and JavaScript frameworks like React.js.</p>
                </div>
                <div class="card">
                    <h3>Weather Site</h3>
                    <p>Created a dynamic weather website using front-end technologies such as HTML5, CSS3, and JavaScript, integrated with a weather API to fetch real-time data.</p>
                </div>
            </div>
        </div>

        <div class="section">
            <h2>Experience</h2>
            <div class="job">
                <h3>AI Intern - Edunet</h3>
                <p>Feb 2025 - Mar 2025 (Virtual)</p>
                <ul>
                    <li>Applied artificial intelligence and machine learning techniques.</li>
                    <li>Develop a Disease Outbreak Prediction Model for three disease.</li>
                    <li>It detects the outbreak of heart problem, parkinsons and diabetes.</li>
                </ul>
            </div>
            <div class="job">
                <h3>Front End Web Developer Intern - Motion Cut</h3>
                <p>Jan 2025 - Feb 2025 (Virtual)</p>
                <ul>
                    <li>Designs various front end projects.</li>
                    <li>Design a E-Commerce homepage clone.</li>
                    <li>Designed a personal bucket list.</li>
                </ul>
            </div>
        </div>

        <div class="section">
            <h2>Education</h2>
            <div class="job">
                <h3>Master of Computer Applications (Expected 2026)</h3>
                <p>PSIT</p>
            </div>
            <div class="job">
                <h3>Bachelor of Computer Application (2021-2024)</h3>
                <p>CSJM University</p>
            </div>
        </div>

        <footer>
            <p>This portfolio was deployed using a custom CI/CD pipeline with GitHub Actions, Docker, and AWS App Runner.</p>
        </footer>
    </div>
</body>
</html>
    """

if __name__ == '__main__':
    # We are still running on port 80 as defined in the Dockerfile
    app.run(host='0.0.0.0', port=80)