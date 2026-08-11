CREATE TABLE `invoices`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `invoice_number` BIGINT NOT NULL,
    `buyer_email` VARCHAR(255) NOT NULL,
    `total_amount` BIGINT NOT NULL
);
ALTER TABLE
    `invoices` ADD UNIQUE `invoices_invoice_number_unique`(`invoice_number`);
CREATE TABLE `products_per_invoice`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `invoice_id` BIGINT NOT NULL,
    `product_id` BIGINT NOT NULL,
    `quantity` INT NOT NULL,
    `unit_price` DECIMAL(8, 2) NOT NULL
);
CREATE TABLE `products`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `price` DECIMAL(8, 2) NOT NULL,
    `entry_date` DATE NOT NULL,
    `brand` VARCHAR(100) NOT NULL,
    `stock_available` INT NOT NULL
);
CREATE TABLE `shopping_carts`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `buyer_email` VARCHAR(255) NOT NULL,
    `status` VARCHAR(255) NOT NULL,
    `created_at` TIMESTAMP NOT NULL,
    `updated_at` TIMESTAMP NOT NULL
);
CREATE TABLE `cart_items`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `cart_id` BIGINT NOT NULL,
    `product_id` BIGINT NOT NULL,
    `quantity` INT NOT NULL
);
ALTER TABLE
    `cart_items` ADD CONSTRAINT `cart_items_cart_id_foreign` FOREIGN KEY(`cart_id`) REFERENCES `shopping_carts`(`id`);
ALTER TABLE
    `products_per_invoice` ADD CONSTRAINT `products_per_invoice_product_id_foreign` FOREIGN KEY(`product_id`) REFERENCES `products`(`id`);
ALTER TABLE
    `cart_items` ADD CONSTRAINT `cart_items_product_id_foreign` FOREIGN KEY(`product_id`) REFERENCES `products`(`id`);
ALTER TABLE
    `products_per_invoice` ADD CONSTRAINT `products_per_invoice_invoice_id_foreign` FOREIGN KEY(`invoice_id`) REFERENCES `invoices`(`id`);