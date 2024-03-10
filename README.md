# SQLSolutions: Requirements and Specification Document

## Project Abstract

In this project, we seek to develop an efficient file system by utilizing a relational database as the underlying storage system. The system will feature a user-friendly web interface enabling users to seamlessly perform basic file system operations in addition to visualizing directories as tree structures. Within its database, the project will store the structure of files and directories, along with metadata such as permissions and creation/update dates. The web application will incorporate user login functionality, ensuring secure management of file system permissions.

## Customer

The ideal customers that this project would target include anyone dealing with user permissions (like IT departments or system administrators), cloud service providers that seek to store files and their metadata efficiently, and small businesses looking for user-friendly file management system that is customizable. In addition, the customer for this project from instructional staff is Abinayaa Kanimozhi Chandrasekar.

## User Requirements

<!--This section lists the behavior that the users see. This information needs to be presented in a logical, organized fashion. It is most helpful if this section is organized in outline form: a bullet list of major topics (e.g., one for each kind of user, or each major piece of system functionality) each with some number of subtopics.-->

| ID   | Description                                                  | Priority | Status |
| ---- | ------------------------------------------------------------ | -------- | ------ |
| 1  | The system must allow the user to create a file. | High     | Open   |
| 2  | The system must allow the user to update the title and contents of any file they have permission to write to. | High     | Open   |
| 3  | The system must allow the user to delete any file they have permission to write to. | High     | Open   |
| 4  | The system must allow the user to view any file they have permission to read. | High     | Open   |
| 5  | The system will present files and directories in human readable fashion. | High     | Open   |
| 6  | The system will allow administrative users to assign file permissions to users. | Medium      | Open   |
| 7  | The system will bar users from editing files they do not have the write permission for. | Medium      | Open   |
| 8  | The system will bar users from deleting files they do not have the write permission for. | Medium      | Open   |
| 9  | The system will bar users from viewing files they do not have the read permission for. | Medium      | Open   |
| 10  | The system will place deleted files into a "recently deleted" folder or "trash bin." | Medium      | Open   |
| 11  | The system will allow the relocation of a file from one directory to another. | Medium      | Open   |
| 12  | The system will allow the copying of a file from one directory to another. | Medium      | Open   |
| 13  | The system will prevent the creation of two files of the same name in the same directory. | Medium     | Open   |
| 14  | The system will allow new users to create a new login with a unique username. | Low      | Open   |
| 15  | The list of files & directories will not be displayed until the user has logged in. | Low     | Open   |
| 16  | The system will allow users to logout of an account. | Low     | Open   |
| 17  | File changes made by the user will persist between login sessions. | Low     | Open   |

## User Stories

<!--Use cases and user stories that support the user requirements in the previous section. The use cases should be based off user stories. Every major scenario should be represented by a use case, and every use case should say something not already illustrated by the other use cases. Diagrams (such as sequence charts) are encouraged. Ask the customer what are the most important use cases to implement by the deadline. You can have a total ordering, or mark use cases with “must have,” “useful,” or “optional.” For each use case you may list one or more concrete acceptance tests (concrete scenarios that the customer will try to see if the use case is implemented).-->

1. As a user of the filesystem, in order to store information on my device, I will create a new file for it. (must have)

2. As a user of the filesystem, in order to access information I've already stored, I will open and read an existing file. (must have)

3. As a user of the filesystem, in order to keep my files up to date, I will edit the contents of an existing file. (must have)

4. As a user of the filesystem, in order to keep my device clutter-free, I will delete files I no longer require. (must have)

5. As a user of the filesystem, in order to locate the file I'm looking for, I will refer to a visualization or list of the file directories. (must have)

6. As a user of the filesystem, I can click on a directory or file to view its contents (must have)

6. As a user of the filesystem, in order to begin creating and managing files, I will create an account. (useful)

7. As a user of the filesystem, in order to access my private files, I will create or login to my existing account. (useful)

8. As a user of the filesystem, in order to prevent others from accessing my files, I will log out of my account. (useful)

9. As a user of the filesystem, I will be able to modify permissions for contents I have full admin access to (useful)

9. As a user of the filesystem, I will be able to upload a new file that contains text (useful)

9. As a user of the filesystem, I will edit the title of an existing file. (optional)

10. As a user of the filesystem, in order to keep my device organized, I will edit the locations/directories of existing files. (optional)

11. As a user of the filesystem, in order to back up my personal data, I will create a copy of an existing file and be able to paste it (or cut it). (optional)

12. As a user of the fileystem, I will view my recently deleted files or directories in a trash folder (optional)

13. As a user of the filesystem, these actions will be executed in a user friendly UI that resembles the file system in an operating system.



## Use Case Diagram

![use case diagram](figures/CS506_Use_Case_Diagram.png)

The user logs in, creating a new account if new, and is brought to the main menu which serves as a visualization of the hierarchical filesystem. From there, the user can either create a new file or perform any of several options upon an existing file, including viewing/reading, updating, and deleting.

### User Interface Requirements
The user should be able to clearly see all CRUD operations that they can do in the interface as well as visualization of a directory and what directory they are currently in. Any optional additional functionalities that are implemented will also be shown here. 

## Security Requirements

<!--Discuss what security requirements are necessary and why. Are there privacy or confidentiality issues? Is your system vulnerable to denial-of-service attacks?-->
The system will ensure that only users with the correct permissions can access the files they have the read or write permissions for. This will allow for more capable system administration. 

## System Requirements

<!--List here all of the external entities, other than users, on which your system will depend. For example, if your system inter-operates with sendmail, or if you will depend on Apache for the web server, or if you must target both Unix and Windows, list those requirements here. List also memory requirements, performance/speed requirements, data capacity requirements, if applicable.-->
As of now, we do not foresee any other entities on which our system will depend. Our system will have performance/speed requirement of giving the user their request within a timely manner (2 seconds or less) if possible.

## Specification

<!--A detailed specification of the system. UML, or other diagrams, such as finite automata, or other appropriate specification formalisms, are encouraged over natural language.-->

<!--Include sections, for example, illustrating the database architecture (with, for example, an ERD).-->

<!--Included below are some sample diagrams, including some example tech stack diagrams.-->

<!--You can make headings at different levels by writing `# Heading` with the number of `#` corresponding to the heading level (e.g. `## h2`).-->

### System Architecture
![database architecture backend](figures/system_architecture_backend.png)

### Database
![database architecture](figures/UPDATED_DB.png)

### Technology Stack (PYTHON):

##### 1.Web Application Framework Decision:
We chose <b>Flask</b> over Django becasue Flask provides more flexibility and is lightweight, which is advantageous for building a simpler, more controlled application. Flask allows us to add only the components we need, avoiding the overhead of Django's more monolithic structure. This leads to clearer and more concise codebase which is particularly beneficial for smaller-scale projects or when starting with a microstrucutre architecture. Bascially, Flask is simpler than Django.

##### 2. Frontend Development Tools:
We are sticking with basic web technologies like <b>HTML, CSS and Javascript</b> because they form the foundation of web development and are sufficient for constructing our application's user interface. This choice allows us to focus on building a functional and responsive design for visualizing the directory tree without the learning curve or complexity that comes with advanced frontend frameworks. We can incorporate <b>React</b> if there is a need for dynamic features.

##### 3. Database Connection and Management:
Although <b>Flask</b> does not come with a built-in ORM like Django, we can use extensions like <b>Flask-SQLAlchemy</b> to integrate ORM capabilities. This enables us to still use <b>Flask's</b> lightweight framework.

##### 4. Authentication and Permission Management:
We are using OAuth for authentication as we have no other choice.

##### 5. Development, Testing and Deployment:
We use <b>Gitlab</b>. This aligns well with Flask's modular approach, allowing us to integrate various tools we need, supporting CI/CD pipelines efficiently.

##### 6. Security Tools:
Flask allows us to be selective about the security tools and extensions we implement. We can use extensions such as <b>Flask-Talisman</b> to secure against XSS and CSRF, and Flask-Security for handling common security mechanisms, giving us the flexibility to tailor our security posture to the exact needs of our application.

##### 7. Server and Hosting Environment:
We opt for web servers like <b>Apache</b> or <b>nginx</b> due to their robustness and <b>Docker</b> for containerization. Docker compliments Flask's simplicity and modularity, allowing us to deploy each microservice or application component in its container.




### Standards & Conventions

<!--Here you can document your coding standards and conventions. This includes decisions about naming, style guides, etc.-->

##### Variables & Naming:

PascalCase for global variable names

camelCase for local variable & method names

ALL-CAPS for constants

No one-letter variable names (with exception of loop control)

##### Documentation:

Minimum one line commented description per method

Use [DocStrings](https://peps.python.org/pep-0257/) for Python

Include descriptive messages upon commit 

##### Formatting:

Maintain proper indentation for readability (necessary for Python)

Keep open brackets inline with method header; closing bracket on its own line

Include one empty line between methods for readability 

##### Error Handling:

All functions that encounter an error condition should either return a 0 or 1 for simplifying the debugging, as well as a descriptive error message
