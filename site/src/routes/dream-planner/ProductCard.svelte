<script lang="ts">
    export let product;
</script>

<section class="product">
    <img src={product.mainImageUrl} alt={product.mainImageAlt} />
    <h2>{product.name}</h2>
    <p class="info">{product.typeName}, {product.itemMeasureReferenceText}</p>
    <p class="price">{product.salesPrice.numeral}:-</p>
</section>

<style lang="scss">
    .product {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;

        * {
            margin: 0;
            padding: 0;
            max-width: 15rem;
        }

        h2 {
            margin-top: 1rem;
            margin-bottom: 1rem;
        }

        .price {
            font-size: 1.2rem;
            font-weight: bold;
            margin-top: .4rem;
            margin-bottom: .4rem;
        }
    }
</style>
