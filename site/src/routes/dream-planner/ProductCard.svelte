<script lang="ts">
    import { fade } from "svelte/transition";

    export let product;

    let infoText = product.typeName;
    if (product.itemMeasureReferenceText != "") {
        infoText = `${infoText}, ${product.itemMeasureReferenceText}`;
    }

    let imageLoad = new Promise<void>((resolve, reject) => {
        const img = new Image();
        img.src = product.mainImageUrl;
        img.onload = () => resolve();
        img.onerror = () => reject(new Error("failed to load image"));
    });
</script>

<a
    class="product"
    href={product.pipUrl}
    target="_blank"
    rel="noopener noreferrer"
>
    <div class="img-container">
        {#await imageLoad then}
            <img
                transition:fade
                src={product.mainImageUrl}
                alt={product.mainImageAlt}
            />
        {/await}
    </div>
    <h2>{product.name}</h2>
    <p class="info">{infoText}</p>
    <p class="price">{product.salesPrice.numeral}:-</p>
</a>

<style lang="scss">
    .product {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
        width: 15rem;

        * {
            margin: 0;
            padding: 0;
        }

        .img-container,
        img {
            display: block;
            aspect-ratio: 1;
            width: 100%;
            object-fit: cover;
        }

        h2 {
            margin-top: 1rem;
            margin-bottom: 1rem;
        }

        .price {
            font-size: 1.2rem;
            font-weight: bold;
            margin-top: 0.4rem;
            margin-bottom: 0.4rem;
        }
    }
</style>
