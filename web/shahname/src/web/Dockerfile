FROM node

WORKDIR /app
COPY . .
RUN npm ci

ENV NODE_ENV=production
RUN chmod +x /app/server.js
CMD ["/app/server.js"]
