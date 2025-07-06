# MCPmed UniProt + Ensembl

## What’s this?

This is a small web app built using Streamlit that lets you search for genes related to diseases or keywords. It pulls info from two popular bioinformatics sources:

-> **UniProt** - for protein and gene names

-> **Ensembl** - for gene locations and details

You just type in a disease or any keyword, and it shows you a list of genes with basic descriptions and where they are on the genome. It also gives you handy links to the full records on UniProt and Ensembl websites.

## Why did I build this?

The task was to develop an MCP client for a bioinformatics website using the official [MCPmed Cookiecutter template](https://github.com/MCPmed/Cookiecutter-MCPmed). This app was created starting from that template to ensure it fits into the MCP ecosystem and follows the recommended structure.

It combines data from UniProt and Ensembl APIs, showing useful gene info with an easy to use web interface powered by Streamlit.

## How to use

- Clone this repo

- Install Python packages from requirements.txt
    - To install the dependencies, run this command in your terminal:
         ```pip install -r requirements.txt```
 This will install all the necessary libraries like streamlit, requests, and any others your app needs.
      
- Run the app using the below command in your terminal:

   ``` streamlit run main.py  ```

- Type your disease or keyword in the box and wait for results

- Click on each gene to see more details and open links to official sites

## What’s inside?

- main.py — main Streamlit app that handles everything

- requirements.txt — list of Python packages needed

The project was bootstrapped using the MCPmed Cookiecutter template to follow best practices and keep things neat

## Notes

- Only shows reviewed human genes from UniProt

- Ensembl API adds gene location info (chromosome, strand, etc.)

- The UI is simple so anyone can use it quickly without tech knowledge

## License

This project is open source under MIT License.




