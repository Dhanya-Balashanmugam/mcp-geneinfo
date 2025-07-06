import requests

def fetch_uniprot_genes(keyword, max_results=5):
    print(f"\n🔍 Searching UniProt for keyword: {keyword}")
    query_url = (
        f"https://rest.uniprot.org/uniprotkb/search?"
        f"query={keyword}+AND+organism_id:9606+AND+reviewed:true&format=json&limit={max_results}"
    )
    response = requests.get(query_url)
    if response.status_code != 200:
        print("❌ Failed to fetch data from UniProt.")
        return []

    results = response.json().get("results", [])
    gene_list = []
    for entry in results:
        gene_symbol = entry.get("genes", [{}])[0].get("geneName", {}).get("value", "Unknown")
        accession = entry.get("primaryAccession", "Unknown")
        description = (
            entry.get("proteinDescription", {})
                 .get("recommendedName", {})
                 .get("fullName", {})
                 .get("value", "No description available.")
        )
        # Build UniProt link for direct access
        uniprot_link = f"https://www.uniprot.org/uniprot/{accession}"

        gene_list.append({
            "gene": gene_symbol,
            "uniprot_id": accession,
            "description": description,
            "uniprot_link": uniprot_link
        })
    return gene_list

def fetch_ensembl_info(gene_symbol):
    ensembl_url = f"https://rest.ensembl.org/lookup/symbol/homo_sapiens/{gene_symbol}?content-type=application/json"
    response = requests.get(ensembl_url)
    if response.status_code != 200:
        return None

    data = response.json()
    # Build Ensembl gene page URL
    ensembl_link = f"https://www.ensembl.org/Homo_sapiens/Gene/Summary?g={data.get('id', '')}"

    return {
        "chromosome": data.get("seq_region_name", "N/A"),
        "start": data.get("start", "N/A"),
        "end": data.get("end", "N/A"),
        "strand": data.get("strand", "N/A"),
        "biotype": data.get("biotype", "N/A"),
        "display_name": data.get("display_name", "N/A"),
        "ensembl_link": ensembl_link
    }

def main():
    print("🧬 MCPmed: UniProt + Ensembl REST API Explorer\n")
    search_term = input("Enter disease or keyword (e.g. cancer, diabetes): ").strip()
    genes = fetch_uniprot_genes(search_term)

    if not genes:
        print("⚠️ No matching genes found.")
        return

    print("\n🧠 Genes and Ensembl gene info:\n")
    for idx, gene in enumerate(genes, 1):
        print(f"{idx}. Gene: {gene['gene']} | UniProt ID: {gene['uniprot_id']}")
        print(f"   🔗 UniProt URL: {gene['uniprot_link']}")
        print(f"   🧬 Description: {gene['description']}")

        ensembl_data = fetch_ensembl_info(gene['gene'])
        if ensembl_data:
            print("   🔬 Ensembl gene info:")
            print(f"       Chromosome: {ensembl_data['chromosome']}")
            print(f"       Location: {ensembl_data['start']} - {ensembl_data['end']}")
            print(f"       Strand: {ensembl_data['strand']}")
            print(f"       Biotype: {ensembl_data['biotype']}")
            print(f"       Display name: {ensembl_data['display_name']}")
            print(f"       🔗 Ensembl URL: {ensembl_data['ensembl_link']}")
        else:
            print("   ⚠️ No Ensembl info found.")
        print()

if __name__ == "__main__":
    main()
