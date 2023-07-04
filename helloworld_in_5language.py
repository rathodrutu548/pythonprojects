
import os
import sys as system

def clear():
    if system.platform.startswith(('win32')):
        os.system('cls')
    elif system.platform.startswith(('linux', 'cygwin', 'darwin', 'freebsd')):
        os.system('clear')

def main():
    clear()
    print("Welcome to how to print hello world in every programming language!")
    print("Programming Languages:\n1. Python\n2. C\n3. C++\n4. C#\n5. Java\n")
    proglang = input("Select a language: (name)\n> ")

    if proglang.lower() == "python":
        print("\nprint(\"Hello World!\")\n")
    elif proglang.lower() == "c":
        print("""\n#include <stdio.h>

int main() {
    printf("Hello World!");
    return 0;
}\n""")
    elif proglang.lower() == "cpp" or proglang.lower == "c++":
        print("""\n#include <iostream>
using namespace std;

int main() {
    cout << "Hello World!";
    return 0;
}\n""")
    elif proglang.lower() == "csharp" or proglang.lower() == "c#    ":
        print("""\nnamespace HelloWorld
{
    class Hello {         
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}\n""")
    elif proglang.lower() == "java":
        print("""\nclass HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); 
    }
\n""")
    else:
        print("Invalid programming language or not added yet.")

main()