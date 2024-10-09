<script async="true" lang="ts">
    const geolocation: Promise<{ city: string; country_name: string }> =
        (async function () {
            const response = await fetch("https://api.ipgeolocation.io/");
            const json = await response.json();
            return json;
        })();
</script>

{#await geolocation}
    Loading...
{:then geolocation}
    It looks like you're browsing from {geolocation.city}, {geolocation.country_name}.
    Is that correct?
{/await}
