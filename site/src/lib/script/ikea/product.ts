export async function fetchProductInfo(id: string) {
    const url = `https://sik.search.blue.cdtapps.com/se/en/search-result-page?q=${id}`;
    const response = await fetch(url);
    const json = await response.json()
    const items = json.searchResultPage.products.main.items;
    if (items[0] == undefined) {
        throw new Error(`no product match for id ${id}`)
    }
    return items[0].product;
}
