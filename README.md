# Welcome to the AirBnB Clone Console!

## Project Overview

The AirBnB Clone Console is a command-line interface (CLI) tool developed as part of the AirBnB Clone Project. This project aims to replicate the core functionalities of the popular Airbnb platform, allowing users to manage accommodations, bookings, user profiles, reviews, and messaging.

### Key Features:

- **Accommodation Management:**
    - Hosts can create detailed listings for their properties, including descriptions, photos, pricing, and availability.
    - Guests can search for listings using various filters like location, dates, amenities, and price range.

- **Booking System:**
    - Hosts can manage availability calendars for their listings.
    - Guests can send booking requests, which hosts can approve or decline.
    - Secure payment processing is integrated for seamless transactions.

- **User Profiles:**
    - Users (both hosts and guests) can create and manage their profiles, providing information, contact details, and verification.

- **Reviews & Ratings:**
    - Both guests and hosts can leave reviews and ratings for each other to build trust within the community.

- **Messaging:**
    - The platform facilitates communication between hosts and guests, enabling them to discuss details, ask questions, and coordinate during the booking process.

## Using the Command Interpreter

### Purpose:
The command interpreter serves as the primary interface for interacting with the AirBnB Clone Console. It allows users to execute various commands to create, retrieve, update, and delete objects within the system.

### Getting Started:

To start the command interpreter, simply execute the `console.py` script from your terminal:

```bash
$ ./console.py 
```
### Available Commands:

    help: Display a list of available commands and their descriptions.
    
    create <class_name>: Create a new object of the specified class.
    
    show <class_name> <object_id>: Display details of a specific object.
    
    update <class_name> <object_id> <attribute> <new_value>: Update the specified attribute of an object.
    
    destroy <class_name> <object_id>: Delete a specific object.
    
    all <class_name>: Display all objects of the specified class.
  
 **Examples:**
  (hbnb) create User
  (hbnb) show Listing 123456
  (hbnb) update Booking 987654 status confirmed
  (hbnb) destroy Review 555555

  **### Exiting the Interpreter:**

To exit the command interpreter, simply use the quit command:

```bash
(hbnb) quit
```
### Contributors

    Twitter
    LinkedIn
    GitHub
