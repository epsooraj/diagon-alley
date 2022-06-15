const ProductResolvers = {
    Query: {
	getAllProducts: () => {
	    return [];
	},
	getProduct(id: ID) => {
	    return {id: 1, name: "jesty"};
	},
    },
}

export default ProductResolvers;

