module.exports = {
    publicPath: "/vcgs_forum/",
    productionSourceMap: process.env.NODE_ENV != 'production',
    outputDir: "docs",
    configureWebpack: {
      optimization: {
        splitChunks: false
      }
    }
}