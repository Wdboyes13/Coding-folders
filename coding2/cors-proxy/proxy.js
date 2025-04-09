const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

app.use(
  '/', 
  createProxyMiddleware({
    target: 'http://localhost:8080/admin/master/console',  // Replace with your target URL
    changeOrigin: true,
    onProxyRes: (proxyRes, req, res) => {
      // Add custom headers to the response
      proxyRes.headers['Access-Control-Allow-Origin'] = '*';  // Allow all origins
      proxyRes.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE';
      proxyRes.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization';
    },
  })
);

app.listen(3000, () => {
  console.log('Proxy server running on http://localhost:3000');
});
