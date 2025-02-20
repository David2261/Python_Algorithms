/*
E. Магические cсылки
Легенда
В одном волшебном королевстве очень злые маги начали подделывать ссылки на ценные знания, находящиеся на сервисах Яндекса. Вашей задачей, как чародея-защитника, является создать заклинание, которое сможет распознавать истинные магические ссылки и блокировать поддельные.

Условиe
Напишите функцию isValidYandexLink(url), которая проверяет, является ли переданная строка параметра url ссылкой на любой из сервисов Яндекса.

1. Ссылка считается валидной, если она ведет на один из доменов, принадлежащих Яндексу.
2. Домен может быть как основным (.ru), так и международным (.by, .com и т.д.).
3. Примеры доменов и поддоменов:
домены: ya.ru, yandex.com, yandex.kz, yandex.by, yandex.az, и т.д.
поддомены: education.yandex., lyceum.yandex., shad.yandex., и т.д.

Примеры
isValidYandexLink("https://ya.ru") // true
isValidYandexLink("https://education.yandex.ru") // true
isValidYandexLink("http://yandex.ru/cup") // true
isValidYandexLink("https://dataschool.yandex.com") // true
isValidYandexLink("https://education.yandex.ru/uchebnik") // true
isValidYandexLink("https://google.com") // false
isValidYandexLink("http://example.com") // false
isValidYandexLink("hts://y*ndex.ru/somepath") // false
- Функция должна возвращать true, если переданная ссылка валидна и ведет на один из сервисов Яндекса.
- Функция должна возвращать false, если переданная ссылка не ведет на сервис Яндекса или если ссылка невалидна (например, htp:/wrong.url).
- Функция должна корректно обрабатывать различные виды URL (с/без http(s), с различными разделителями и параметрами).

Формат ввода
function isValidYandexLink(url) {
    // Your code here...
}

module.exports = isValidYandexLink;
*/

function isValidYandexLink(url) {
    if (!url) {
        return false;
    }

    try {
        const urlObj = new URL(url); // Пытаемся создать объект URL для парсинга
        const hostname = urlObj.hostname; // Получаем имя хоста (домен)

        if (!hostname) {
            return false; // Если имя хоста не определено, ссылка невалидна
        }
      
        const allowedDomains = [
            "ya.ru", "yandex.ru", "yandex.ua", "yandex.by", "yandex.kz",
            "yandex.com", "yandex.az", "yandex.ge", "yandex.kg", "yandex.md",
            "yandex.tj", "yandex.tm", "yandex.uz"
        ];
      
        // Проверяем, что домен или поддомен входит в список разрешенных
        const hostnameParts = hostname.split('.');
        
        for (let i = 0; i < hostnameParts.length; i++) {
            const domainToCheck = hostnameParts.slice(i).join('.');
            if (allowedDomains.includes(domainToCheck)) {
                return true;
            }
        }

        return false; // Домен не найден в списке разрешенных

    } catch (error) {
        return false; // Если URL невалидный, возвращаем false
    }
}

module.exports = isValidYandexLink;