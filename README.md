# Микросервисная система обработки заказов

## Описание

Система состоит из трёх микросервисов, взаимодействующих по HTTP внутри общей Docker-сети.  
Заказ создаётся через **Order Service**, который последовательно запрашивает данные о товаре у **Product Service** и рассчитывает скидку через **Discount Service**.

### Сервисы

| Сервис | Назначение | Внутренний порт |
|--------|------------|-----------------|
| **Product Service** | Хранит каталог товаров и их базовые цены | `8000` |
| **Discount Service** | Рассчитывает скидку на основе промокода и количества товара | `8000` |
| **Order Service** | Оркестратор: принимает заказ, собирает данные, возвращает итоговую детализацию | `8000` (наружу проброшен порт `8002`) |

### Логика работы Order Service

1. Принимает `POST /orders` с `product_id`, `quantity` и опциональным `promo_code`.
2. Запрашивает у **Product Service** информацию о товаре (`GET /products/{product_id}`).
3. Передаёт данные в **Discount Service** (`POST /discounts/calculate`) для получения процента скидки и причины.
4. Рассчитывает итоговую стоимость и возвращает полную детализацию.

### Правила расчёта скидки (Discount Service)

- Если передан промокод `STUDENT10` — скидка **10%**.
- Если количество товара ≥ 10 — скидка **15%** (оптовая).
- Если условий нет — скидка **0%**.

### Предустановленные товары (Product Service)

| ID | Название | Цена | Доступен |
|----|----------|------|----------|
| `pencil` | Pencil | 1.50 | ✅ |
| `notebook` | Notebook | 4.20 | ✅ |
| `backpack` | Backpack | 35.00 | ❌ (нет в наличии) |

---

## Запуск

### Требования

- Docker
- Docker Compose (опционально, но рекомендуется)

### Вариант 1: Docker Compose (рекомендуемый)

```bash
# Сборка и запуск всех сервисов
docker compose up --build
```

После запуска **Order Service** будет доступен на `http://localhost:8002`.  
Остальные сервисы доступны только внутри сети Docker.

### Вариант 2: Ручной запуск через `docker run`

1. Создайте общую сеть:

```bash
docker network create orders-network
```

2. Соберите образы для каждого сервиса (из соответствующих директорий):

```bash
docker build -t product-service ./product_service
docker build -t discount-service ./discount_service
docker build -t order-service ./order_service
```

3. Запустите контейнеры:

```bash
docker run -d --name product-service --network orders-network product-service
docker run -d --name discount-service --network orders-network discount-service
docker run -d --name order-service --network orders-network \
  -p 8002:8000 \
  -e PRODUCT_SERVICE_IP=http://product-service \
  -e PRODUCT_SERVICE_PORT=8000 \
  -e DISCOUNT_SERVICE_IP=http://discount-service \
  -e DISCOUNT_SERVICE_PORT=8000 \
  order-service
```

---

## Проверка работы

Отправьте `POST`-запрос к **Order Service**:

```bash
curl -X POST http://localhost:8002/orders \
  -H "Content-Type: application/json" \
  -d '{
    "product_id": "notebook",
    "quantity": 10,
    "promo_code": "STUDENT10"
  }'
```

**Пример ответа:**

```json
{
  "product_id": "notebook",
  "quantity": 10,
  "unit_price": 4.2,
  "total_before_discount": 42.0,
  "discount_percent": 15.0,
  "discount_amount": 6.3,
  "total_after_discount": 35.7,
  "discount_reason": "Bulk order discount"
}
```

> **Примечание:** Если одновременно срабатывают промокод и оптовая скидка, применяется только одна из них (в текущей реализации приоритет у промокода).

Другие тестовые запросы:

- Товар не найден: `{"product_id": "unknown", "quantity": 1}`
- Товар недоступен: `{"product_id": "backpack", "quantity": 1}`
- Сервис скидок недоступен (если остановить `discount-service`): вернётся `503 Service Unavailable`.

---

## Переменные окружения

**Order Service** использует следующие переменные для адресации других сервисов:

| Переменная | Значение по умолчанию | Описание |
|------------|----------------------|----------|
| `PRODUCT_SERVICE_IP` | `http://127.0.0.1` | IP/имя хоста Product Service |
| `PRODUCT_SERVICE_PORT` | `8001` | Порт Product Service |
| `DISCOUNT_SERVICE_IP` | `http://127.0.0.1` | IP/имя хоста Discount Service |
| `DISCOUNT_SERVICE_PORT` | `8003` | Порт Discount Service |

Внутри Docker Compose эти переменные задаются явно (см. `docker-compose.yml`).

---

## Диагностика сетевого взаимодействия

Подробный отчёт о различиях между локальным запуском, обращением к `localhost` из контейнера, работой через Docker DNS и `host.docker.internal` приведён в файле [`NETWORKING_NOTES.md`](./NETWORKING_NOTES.md).

---

## Структура репозитория

```
fossdev/
├── product_service/       # Исходный код Product Service
│   ├── Dockerfile
│   ├── pyproject.toml
│   └── src/app/main.py
├── discount_service/      # Исходный код Discount Service
│   ├── Dockerfile
│   ├── pyproject.toml
│   └── src/app/main.py
├── order_service/         # Исходный код Order Service
│   ├── Dockerfile
│   ├── pyproject.toml
│   └── src/app/main.py
├── docker-compose.yml     # Описание оркестрации
├── NETWORKING_NOTES.md    # Отчёт о сетевых сценариях
├── .gitignore
└── README.md              # Данный файл