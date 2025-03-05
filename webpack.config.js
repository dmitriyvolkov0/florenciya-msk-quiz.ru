const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
    entry: './_site/src/js/app.js', // Точка входа
    output: {
        path: path.resolve(__dirname, '_site/static'), // Путь для выходных файлов
        filename: 'js/index.js', // Имя выходного JS файла
        clean: true, // Очищает папку перед сборкой
    },
    module: {
        rules: [
            {
                test: /\.scss$/, // Обработка SCSS
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    'sass-loader',
                ],
            },
            {
                test: /\.js$/, // Обработка JavaScript
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env'],
                    },
                },
            },
        ],
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'css/styles.css', // Имя выходного CSS файла
        }),
        new CopyWebpackPlugin({
            patterns: [
                {
                    from: 'modules/**/img/*', // Исходная папка с изображениями
                    to: ({ absoluteFilename }) => {
                        // Удаляем часть пути до "img/" и сохраняем остальную структуру
                        const relativePath = path.relative(
                            path.resolve(__dirname, 'modules'),
                            path.dirname(absoluteFilename)
                        );
                        return `modules/${relativePath.replace(/\/?img$/, '')}/[name][ext]`;
                    },
                },
            ],
        }),
    ],
    devServer: {
        static: path.resolve(__dirname, '_site/static'), // Путь к статическим файлам
        port: 8080, // Порт для сервера
        hot: true, // Горячая замена модулей
    },
    resolve: {
        alias: {
            '@modules': path.resolve(__dirname, 'modules'), // Алиас для модулей
            '@img': path.resolve(__dirname, '_site/src/img'),
        },
    },
};