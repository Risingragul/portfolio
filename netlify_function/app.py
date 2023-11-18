from flask import Flask, render_template_string,request
app = Flask(__name__)
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = 'risingragul@gmail.com'
smtp_pass = ''
# Sample projects data
projects = [
    {
        "title": "Personal Expense Tracker Application",
        "description": "The Personal Expense Tracker lets users monitor daily, monthly,and yearly expenses. It updates their wallet balance in real-time as they input expenses, offering visual spending insights. Users can set monthly limits, and the app sends email alerts if exceeded, ensuring effective budget management and financial awareness.",
        "TechStack": "Tech Stack : Python Flask, Html, CSS, JavaScript, IBM Cloud",
    },
    {
        "title": "Nutro Assistant Application",
        "description": "The Nutro Assistant, a user-friendly meal planning app, offers swift recipe browsing, answers to food queries, and relaxation content. You can explore calorie-based recipe searches, tailor ingredient quantities, and access comprehensive nutrient details. It streamlines meal preparation, encourages healthier dietary choices, and provides a serene culinary experience.",
        "TechStack": " Tech Stack : Html, CSS, JavaScript, Java, MySQL ,Rapid API .",
    },
     {
        "title": "Walking Aid For Visually Impaired",
        "description": "Our innovative smart walking stick addresses challenges faced by visually impaired travelers. Equipped with advanced sensors, including temperature and moisture detectors, an accelerometer, and Bluetooth communication, it offers real-time feedback. Integration with a mobile app provides GPS-based directions and health monitoring, enhancing safety and support for visually impaired individuals.",
        "TechStack": " Tech Stack : Arduino IDE, Mobile app,VoicePlaybackboard, Ultrasonic Sensor ,Water Sensor ,Accelerometer,Vibration Sensor ,Heart-Rate Sensor .",
    },
    {
        "title" : "DevOps CI/CD Pipeline Implementation Project",
        "description":" I successfully implemented an end-to-end DevOps Continuous Integration/Continuous Deployment (CI/CD) pipeline, employing a suite of essential tools and technologies. This included Git and GitHub for code versioning and collaboration, Jenkins for automated code integration and Maven for efficient builds. Continuous code quality checks were ensured with SonarQube, while Docker containerization provided consistent and reliable deployments. GitHub Hooks automatically triggered Jenkins builds upon code commits. Artifact management was streamlined using Nexus Repository Manager. Our application instances were hosted on AWS EC2, with stringent access controls managed through AWS IAM. This initiative significantly improved development efficiency, reduced manual intervention, and enhanced deployment reliability, showcasing proficiency in DevOps best practices and key technologies.",
        "TechStack" : "Tech Stack : Git, GitHub, Jenkins, Maven, SonarQube, Docker, GitHub Hooks, Nexus Repository Manager, AWS EC2, IAM ",
    },
     {
        "title": "AWS S3 Event Triggering Project",
        "description": " Implemented AWS S3 event triggering to automate processes based on changes in S3 buckets. Utilized AWS Lambda functions to respond to specific events such as file uploads or deletions. Configured IAM roles to ensure secure access controls. Enhanced system notifications and responsiveness with Amazon SNS integration. This project demonstrated proficiency in event-driven architectures, AWS services, and secure cloud automation",
        "TechStack": " Tech Stack : AWS S3, AWS Lambda, AWS IAM, Amazon SNS.",
    },

]

@app.route("/")
def home():
    return render_template_string(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>RAGUL C - Portfolio</title>
            <style>
                /* Add your CSS styles here */
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                }
                header {
                    background-color: #333;
                    color: white;
                    padding: 20px;
                    text-align: center;
                }
                nav ul {
                    list-style-type: none;
                    padding: 0;
                }
                nav ul li {
                    display: inline;
                    margin-right: 20px;
                }
                main {
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: white;
                }
                section#projects ul {
                    list-style-type: none;
                    padding: 0;
                }
                section#projects ul li {
                    margin-bottom: 20px;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>RAGUL C - Portfolio</h1>
                <p>Welcome to my portfolio website.</p>
            </header>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/contact">Contact</a></li>
                    <li><a href="/resume">Resume</a></li>
                </ul>
            </nav>
            <main>
                <section id="projects">
                   <h2> <center>  My Projects <center></h2>
                    <ul>
                        {% for project in projects %}
                        <li>
                           <u> <h3>{{ project.title }}</h3></u>
                            <p>{{ project.description }}</p>
                            <h3> {{ project.TechStack}}</h3>
                            <hr>
                        </li>
                        {% endfor %}
                    </ul>
                </section>
            </main>
            <footer>
            <p><center>&copy; {{ 2023 }} RR </center></p>
            </footer>
        </body>
        </html>
        """,
        projects=projects,
    )

@app.route("/about")
def about():
    return render_template_string(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>About Me</title>
            <style>
                /* Add your CSS styles here */
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                }
                header {
                    background-color: #333;
                    color: white;
                    padding: 20px;
                    text-align: center;
                }
                nav ul {
                    list-style-type: none;
                    padding: 0;
                }
                nav ul li {
                    display: inline;
                    margin-right: 20px;
                }
                main {
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: white;
                }
            </style>
        </head>
        <body>
            <header>
                <h2>About Me</h2>
                <p>About  my technical skills.</p>
            </header>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/contact">Contact</a></li>
                    <li><a href="/resume">Resume</a></li>
                </ul>
            </nav>
            <main>
    <style>
        /* Add your CSS styles here */
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #333;
            color: white;
            padding: 20px;
            text-align: center;
        }
        main {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: white;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        ul {
            list-style-type: square;
            padding-left: 20px;
        }
        li {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>

        <h1><u>Technical Skills</u></h1>

    <main>
        <h2>Programming Languages</h2>
        <ul>
            <li>Python</li>
            <li>Java</li>
            <li>C</li>
            <li>Shell Script</li>
        </ul>

        <h2>Front End Technologies</h2>
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
            <li>ReactJs</li>
            <li>JQuery</li>
            <li>Bootstrap</li>
        </ul>

        <h2>Back End Technologies</h2>
        <ul>
            <li>MySQL</li>
            <li>MongoDB</li>
        </ul>

        <h2>Cloud Tech</h2>
        <ul>
            <li>AWS Services</li>
            <ul>
                <li>S3</li>
                <li>EC2</li>
                <li>IAM</li>
                <li>VPC</li>
                <li>RDS</li>
                <li>Route 53 (R53)</li>
                <li>RDS</li>
                <li>ELB & ASG</li>
                <li>SNS,SQS,CW</li>
                <li>CI\CD</li>
                <li>Cloud Front</li>
                <li>Cloud Trail</li>
                <li>Lambda</li>
                <li>Migration & SnowBall</li>


            </ul>
        </ul>

        <h2>DevOps</h2>
        <ul>
        <li>Git</li>
            <li>Github</li>
            <li>Maven</li>
            <li>Sonarqube</li>
            <li>Jenkins</li>
            <li>Ansible</li>
            <li>Docker</li>
            <li>Kubernetes</li>
            <li>Terraform</li>
            <li>Prometheus</li>
            <li>Garfana</li>
            <li>Nagios</li>
            <li>Splunk</li>
        </ul>
         <h2>Operating System</h2>
        <ul>
            <li>Windows</li>
            <li>Linux</li>
            <li>Ubuntu</li>
        </ul>
    </main>
</body>

            </main>
            <footer>
                <p><center>&copy; {{ 2023 }} RR </center></p>
            </footer>
        </body>
        </html>
        """
    )



html_template ="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 500px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="email"],
        textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        textarea {
            resize: vertical;
            height: 100px;
        }
        input[type="submit"] {
            background-color: #333;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #555;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Contact Us</h1>
        <form action="/contactme" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4" required></textarea>

            <input type="submit" value="Submit">
        </form>
    </div>
</body>
</html>
"""

@app.route('/contactme', methods=['GET', 'POST'])
def contact_form():
        if request.method == 'POST':
            sender_email = request.form['email']
            name = request.form['name']
            subject = 'Contact Mail'
            message = request.form['message']

        # Create the MIMEText object
        msg = MIMEMultipart()
        msg['From'] = 'support@gmail.com'
        msg['To'] = sender_email
        msg['Subject'] = subject

        # HTML content with placeholders for sender's email and message
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form Submission</title>
</head>
<body>
    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px;">
        <h2>Contact Form</h2>
        <p>You've received a message from the contact:</p>
        <p><strong>From:</strong> {sender_email}</p>
        <p><strong>Message:</strong></p>
        <div>
            <b>{message}</b>
        </div>
        <p>Feel free to respond to this email to get in touch with the sender.</p>
    </div>
</body>
</html>
"""

        # Attach the HTML content as an HTML part
        html_part = MIMEText(html_content, 'html')
        msg.attach(html_part)

        try:
            # Establish a secure connection with the SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()

            # Log in to your Gmail account
            server.login(smtp_user, smtp_pass)

            # Send the email with the attached HTML content
            server.sendmail('support@gmail.com', sender_email, msg.as_string())
            server.quit()

            # You can return a confirmation message or redirect to a success page
            return 'Email sent successfully'
        except Exception as e:
            return 'Error Occurs: ' + str(e)

        return render_template_string(html_template)
@app.route("/contact")
def contact():
    return render_template_string(
        """
       <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Me</title>
    <style>
        /* Add your CSS styles here */
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }
        header {
            background-color: #333;
            color: white;
            padding: 20px;
            text-align: center;
        }
        nav ul {
            list-style-type: none;
            padding: 0;
        }
        nav ul li {
            display: inline;
            margin-right: 20px;
        }
        main {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: white;
        }

        /* New styles for form elements */
        form {
            margin-top: 20px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="email"],
        textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        textarea {
            resize: vertical;
            height: 100px;
        }
        input[type="submit"] {
            background-color: #333;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #555;
        }
    </style>
</head>
<body>
    <header>
        <h1>Contact Me</h1>
        <p>Feel free to get in touch with me.</p>
    </header>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/contact">Contact</a></li>
            <li><a href="/resume">Resume</a></li>
        </ul>
    </nav>
    <main>
        <div class="container">
            <h1>Contact Us</h1>
            <form action="/contactme" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" required></textarea>

                <input type="submit" value="Submit">
            </form>
        </div>
    </main>
    <footer>
       <p><center>&copy; {{ 2023 }} RR </center></p>
    </footer>
</body>
</html>

        """
    )

@app.route("/resume")
def resume():
    # You can provide a link to your resume file or embed it directly.
    resume_link = "https://drive.google.com/file/d/1uyDTIFcoJlXFquyxFFUFbIME9hdiZzdq/view?usp=sharing"
    return render_template_string(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>
                        My Resume</title>
            <style>
                /* Add your CSS styles here */
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                }
                header {
                    background-color: #333;
                    color: white;
                    padding: 20px;
                    text-align: center;
                }
                nav ul {
                    list-style-type: none;
                    padding: 0;
                }
                nav ul li {
                    display: inline;
                    margin-right: 20px;
                }
                main {
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: white;
                }
            </style>
        </head>
        <body>
            <header>
                <h1>My Resume</h1>
                <p>View or download my resume.</p>
            </header>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/contact">Contact</a></li>
                    <li><a href="/resume">Resume</a></li>
                </ul>
            </nav>
            <main>
                <center><a href="{{ resume_link }}" target="_blank">Download Resume</a><center>
            </main>
        </body>
        </html>
        """,
        resume_link=resume_link,
    )

if __name__ == "__main__":
    app.run(debug=True)
