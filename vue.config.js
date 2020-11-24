module.exports = {
    publicPath: ".",
    productionSourceMap: process.env.NODE_ENV != 'production',
    configureWebpack: {
      optimization: {
        splitChunks: false
      }
    }
}