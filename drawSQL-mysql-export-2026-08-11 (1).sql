CREATE TABLE `invoices`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `invoice_number` BIGINT NOT NULL,
    `buyer_email` VARCHAR(255) NOT NULL,
    `total_amount` BIGINT NOT NULL,
    `user_id` BIGINT NOT NULL,
    `payment_method_id` BIGINT NOT NULL
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
CREATE TABLE `users`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `email_user` VARCHAR(255) NOT NULL,
    `registration_date` DATE NOT NULL
);
ALTER TABLE
    `users` ADD UNIQUE `users_email_user_unique`(`email_user`);
CREATE TABLE `reviews`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `review_id` BIGINT NOT NULL,
    `product_code` BIGINT NOT NULL,
    `comment` VARCHAR(255) NOT NULL,
    `rating` DECIMAL(8, 2) NOT NULL,
    `date` DATE NOT NULL,
    `user_id` BIGINT NOT NULL
);
CREATE TABLE `payment_methods`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `method_type` VARCHAR(255) NOT NULL,
    `bank_name` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `reviews` ADD CONSTRAINT `reviews_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `users`(`id`);
ALTER TABLE
    `invoices` ADD CONSTRAINT `invoices_payment_method_id_foreign` FOREIGN KEY(`payment_method_id`) REFERENCES `payment_methods`(`id`);
ALTER TABLE
    `cart_items` ADD CONSTRAINT `cart_items_cart_id_foreign` FOREIGN KEY(`cart_id`) REFERENCES `shopping_carts`(`id`);
ALTER TABLE
    `products_per_invoice` ADD CONSTRAINT `products_per_invoice_product_id_foreign` FOREIGN KEY(`product_id`) REFERENCES `products`(`id`);
ALTER TABLE
    `invoices` ADD CONSTRAINT `invoices_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `users`(`id`);
ALTER TABLE
    `cart_items` ADD CONSTRAINT `cart_items_product_id_foreign` FOREIGN KEY(`product_id`) REFERENCES `products`(`id`);
ALTER TABLE
    `reviews` ADD CONSTRAINT `reviews_product_code_foreign` FOREIGN KEY(`product_code`) REFERENCES `products`(`id`);
ALTER TABLE
    `products_per_invoice` ADD CONSTRAINT `products_per_invoice_invoice_id_foreign` FOREIGN KEY(`invoice_id`) REFERENCES `invoices`(`id`);