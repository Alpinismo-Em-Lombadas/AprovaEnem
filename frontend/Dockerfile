FROM node:24-alpine

WORKDIR /app

# Instala as dependências antes de copiar o código para aproveitar o cache do Docker
COPY package.json package-lock.json ./
RUN npm ci

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]
