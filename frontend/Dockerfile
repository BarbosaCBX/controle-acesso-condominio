# Estágio de Produção com Nginx Alpine (imagem leve)
FROM nginx:1.26-alpine

# Copia os arquivos estáticos da aplicação para a pasta padrão do Nginx
COPY ./public /usr/share/nginx/html/public
COPY ./src /usr/share/nginx/html/src
COPY ./public/index.html /usr/share/nginx/html/index.html

# Copia a configuração customizada do Nginx
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]