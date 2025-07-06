import streamlit as st
import requests

def fetch_uniprot(keyword, limit=10):
    url = f"https://rest.uniprot.org/uniprotkb/search?query={keyword}+AND+organism_id:9606+AND+reviewed:true&format=json&limit={limit}"
    response = requests.get(url)
    if response.status_code != 200:
        st.error("UniProt search failed.")
        return []

    data = response.json()
    genes = []
    for entry in data.get("results", []):
        gene_name = entry.get("genes", [{}])[0].get("geneName", {}).get("value", "N/A")
        uniprot_id = entry.get("primaryAccession", "N/A")
        description = entry.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {}).get("value", "No description available.")
        genes.append({
            "gene": gene_name,
            "uniprot_id": uniprot_id,
            "description": description
        })
    return genes

def fetch_ensembl(gene_symbol):
    url = f"https://rest.ensembl.org/lookup/symbol/homo_sapiens/{gene_symbol}?content-type=application/json"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    return {
        "chromosome": data.get("seq_region_name", "N/A"),
        "start": data.get("start", "N/A"),
        "end": data.get("end", "N/A"),
        "strand": data.get("strand", "N/A"),
        "biotype": data.get("biotype", "N/A"),
        "display_name": data.get("display_name", "N/A"),
        "ensembl_id": data.get("id", None)
    }

def main():
    st.title("🧬 MCPmed: UniProt + Ensembl Gene Info")

    keyword = st.text_input("Enter disease or keyword (e.g. cancer, diabetes):")

    if keyword:
        with st.spinner("Searching UniProt..."):
            genes = fetch_uniprot(keyword)

        if not genes:
            st.warning("No genes found for this keyword.")
            return

        st.header("🧠 Genes and Ensembl Gene Info:")

        for i, gene in enumerate(genes, 1):
            with st.expander(f"{i}. {gene['gene']} | UniProt ID: {gene['uniprot_id']}"):
                st.markdown(f"**Description:** {gene['description']}")
                # Link to UniProt
                uniprot_url = f"https://www.uniprot.org/uniprot/{gene['uniprot_id']}"
                st.markdown(f"[View UniProt entry]({uniprot_url})")

                with st.spinner(f"Fetching Ensembl info for {gene['gene']}..."):
                    ensembl_info = fetch_ensembl(gene['gene'])

                if ensembl_info:
                    st.markdown(
                        f"""
                        **Ensembl gene info:**  
                        - Chromosome: {ensembl_info['chromosome']}  
                        - Location: {ensembl_info['start']} - {ensembl_info['end']}  
                        - Strand: {ensembl_info['strand']}  
                        - Biotype: {ensembl_info['biotype']}  
                        - Display name: {ensembl_info['display_name']}  
                        """
                    )
                    # Link to Ensembl
                    if ensembl_info['ensembl_id']:
                        ensembl_url = f"https://www.ensembl.org/Homo_sapiens/Gene/Summary?g={ensembl_info['ensembl_id']}"
                        st.markdown(f"[View Ensembl entry]({ensembl_url})")
                else:
                    st.warning("No Ensembl info found.")

if __name__ == "__main__":
    main()
