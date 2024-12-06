import java.util.Scanner;

public class PhoneBookApp {
     public static void main(String[] args) {

    static String[] firstNames = new String[100];
    static String[] lastNames = new String[100];
    static String[] phoneNumbers = new String[100];
    static int contactCount = 0;
        Scanner scanner = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\nPhone Book Menu:");
            System.out.println("1. Add contact");
            System.out.println("2. Remove contact");
            System.out.println("3. Find contact by phone number");
            System.out.println("4. Find contact by first name");
            System.out.println("5. Find contact by last name");
            System.out.println("6. Edit contact");
            System.out.println("7. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            scanner.nextLine(); 

            switch (choice) {
                case 1:
                    addContact(scanner);
                    break;
                case 2:
                    removeContact(scanner);
                    break;
                case 3:
                    findContactByPhoneNumber(scanner);
                    break;
                case 4:
                    findContactByFirstName(scanner);
                    break;
                case 5:
                    findContactByLastName(scanner);
                    break;
                case 6:
                    editContact(scanner);
                    break;
                case 7:
                    System.out.println("Exiting the Phone Book App.");
                    break;
                default:
                    System.out.println("Invalid choice, please try again.");
            }
        } while (choice != 7);

        
    }

    
    static void addContact(Scanner scanner) {
        if (contactCount < 100) {
            System.out.print("Enter first name: ");
            firstNames[contactCount] = scanner.nextLine();
            System.out.print("Enter last name: ");
            lastNames[contactCount] = scanner.nextLine();
            System.out.print("Enter phone number: ");
            phoneNumbers[contactCount] = scanner.nextLine();
            contactCount++;
            System.out.println("Contact added successfully!");
        } else {
            System.out.println("Phone book is full!");
        }
    }

    static void removeContact(Scanner scanner) {
        System.out.print("Enter phone number to remove: ");
        String phoneToRemove = scanner.nextLine();
        boolean found = false;

        for (int i = 0; i < contactCount; i++) {
            if (phoneNumbers[i].equals(phoneToRemove)) {
                found = true;
                for (int j = i; j < contactCount - 1; j++) {
                    firstNames[j] = firstNames[j + 1];
                    lastNames[j] = lastNames[j + 1];
                    phoneNumbers[j] = phoneNumbers[j + 1];
                }
                contactCount--;
                System.out.println("Contact removed successfully!");
                break;
            }
        }
        if (!found) {
            System.out.println("Contact with that phone number not found.");
        }
    }

    
    static void findContactByPhoneNumber(Scanner scanner) {
        System.out.print("Enter phone number to find: ");
        String phoneToFind = scanner.nextLine();
        boolean found = false;

        for (int i = 0; i < contactCount; i++) {
            if (phoneNumbers[i].equals(phoneToFind)) {
                found = true;
                System.out.println("Contact found: " + firstNames[i] + " " + lastNames[i] + " - " + phoneNumbers[i]);
                break;
            }
        }
        if (!found) {
            System.out.println("Contact with that phone number not found.");
        }
    }

    
    static void findContactByFirstName(Scanner scanner) {
        System.out.print("Enter first name to find: ");
        String firstNameToFind = scanner.nextLine();
        boolean found = false;

        for (int i = 0; i < contactCount; i++) {
            if (firstNames[i].equalsIgnoreCase(firstNameToFind)) {
                found = true;
                System.out.println("Contact found: " + firstNames[i] + " " + lastNames[i] + " - " + phoneNumbers[i]);
            }
        }
        if (!found) {
            System.out.println("No contact found with that first name.");
        }
    }

   
    static void findContactByLastName(Scanner scanner) {
        System.out.print("Enter last name to find: ");
        String lastNameToFind = scanner.nextLine();
        boolean found = false;

        for (int i = 0; i < contactCount; i++) {
            if (lastNames[i].equalsIgnoreCase(lastNameToFind)) {
                found = true;
                System.out.println("Contact found: " + firstNames[i] + " " + lastNames[i] + " - " + phoneNumbers[i]);
            }
        }
        if (!found) {
            System.out.println("No contact found with that last name.");
        }
    }

  
    static void editContact(Scanner scanner) {
        System.out.print("Enter phone number of the contact to edit: ");
        String phoneToEdit = scanner.nextLine();
        boolean found = false;

        for (int i = 0; i < contactCount; i++) {
            if (phoneNumbers[i].equals(phoneToEdit)) {
                found = true;
                System.out.println("Editing contact: " + firstNames[i] + " " + lastNames[i] + " - " + phoneNumbers[i]);
                System.out.print("Enter new first name: ");
                firstNames[i] = scanner.nextLine();
                System.out.print("Enter new last name: ");
                lastNames[i] = scanner.nextLine();
                System.out.print("Enter new phone number: ");
                phoneNumbers[i] = scanner.nextLine();
                System.out.println("Contact updated successfully!");
                break;
            }
        }
        if (!found) {
            System.out.println("No contact found with that phone number.");
        }
    }
}
