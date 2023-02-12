using System;
using System.Collections.Generic;

namespace PayrollManagementSystem
{
    class Employee
    {
        public string Name { get; set; }
        public int ID { get; set; }
        public double Salary { get; set; }
        public double TaxPercent { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            List<Employee> employees = new List<Employee>();
            while (true)
            {
                Console.WriteLine("Enter 1 to add employee information");
                Console.WriteLine("Enter 2 to calculate payroll");
                Console.WriteLine("Enter 3 to generate pay stub");
                Console.WriteLine("Enter 4 to exit");

                int choice = int.Parse(Console.ReadLine());

                if (choice == 1)
                {
                    Employee emp = new Employee();
                    Console.WriteLine("Enter employee name: ");
                    emp.Name = Console.ReadLine();
                    Console.WriteLine("Enter employee ID: ");
                    emp.ID = int.Parse(Console.ReadLine());
                    Console.WriteLine("Enter employee salary: ");
                    emp.Salary = double.Parse(Console.ReadLine());
                    Console.WriteLine("Enter employee tax percentage: ");
                    emp.TaxPercent = double.Parse(Console.ReadLine());
                    employees.Add(emp);
                    Console.WriteLine("Employee information added successfully.");
                }
                else if (choice == 2)
                {
                    Console.WriteLine("Enter employee ID: ");
                    int id = int.Parse(Console.ReadLine());
                    Employee emp = employees.Find(x => x.ID == id);
                    if (emp != null)
                    {
                        double taxAmount = emp.Salary * (emp.TaxPercent / 100);
                        double netSalary = emp.Salary - taxAmount;
                        Console.WriteLine("Employee name: " + emp.Name);
                        Console.WriteLine("Gross Salary: " + emp.Salary);
                        Console.WriteLine("Tax Amount: " + taxAmount);
                        Console.WriteLine("Net Salary: " + netSalary);
                    }
                    else
                    {
                        Console.WriteLine("Employee not found.");
                    }
                }
                else if (choice == 3)
                {
                    Console.WriteLine("Enter employee ID: ");
                    int id = int.Parse(Console.ReadLine());
                    Employee emp = employees.Find(x => x.ID == id);
                    if (emp != null)
                    {
                        double taxAmount = emp.Salary * (emp.TaxPercent / 100);
                        double netSalary = emp.Salary - taxAmount;
                        Console.WriteLine("Pay Stub for " + emp.Name + ":");
                        Console.WriteLine("Gross Salary: " + emp.Salary);
                        Console.WriteLine("Tax Amount: " + taxAmount);
                        Console.WriteLine("Net Salary: " + netSalary);
                    }
                    else
                    {
                        Console.WriteLine("Employee not found.");
                    }
                }
                else if (choice == 4)
                {
                break;
                }
                else
                {
                Console.WriteLine("Invalid option selected. Please try again.");
                }
            }
        }
    }
}