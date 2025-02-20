/*
D. Внедрение кэширования
После запуска проекта выяснилось, что у пользователей наблюдаются проблемы с памятью при длительном использовании приложения. Результаты, полученные на предыдущих запросах к бэкенду, остаются в памяти, что приводит к зависанию страницы и прочим неприятным последствиям.

Ваша команда разработала план, и вам поручили исправить эту проблему и реализовав его. План заключается в том, чтобы разработать алгоритм кэширования.

Нужно написать функцию, которая получает на вход размер кэша и возвращает интерфейс для встраивания в проект, который будет управлять кэшированием данных на странице. В процессе обсуждений было решено использовать приоритетное кэширование, где дольше сохраняются в кэше те данные, которые использовались последними.



interface EntityDataI<Data extends {id: number}> {
  setCacheChunk: (value: Data | Data[]): void;
  changeItem: (newData: Data | Data[]): void;
  getCacheItemById: (id: number): Data;
  getData: (): Data[];
}
setCacheChunk — Функция чтобы положить новую порцию данных с сервера в кэш;
changeItem — Функция для пользовательского изменения кэшированных данных;
getCacheItemById — Функция для получения элемента из кэша по id;
getAppCache — Функция для получения текущего состояния кэша;
В результате у вас должна получится следующая функция:

module.exports = function getCache(maxSize) {
  // Ваш JavaScript код
}
Пример использования

const cache = getCache(3); // Размер кэша равен трем элементам

cache.setCacheChunk({id: 1}); // Добавляем 1 объект в кэш
cache.setCacheChunk([{id: 2}, {id: 3}]); // Добавляем несколько объектов в кэш
cache.getData() // [{id: 1}, {id: 2}, {id: 3}]

cache.setCacheChunk({id: 4}); // Добавляем 1 объект в заполненный кэш
cache.getData() // [{id: 2}, {id: 3}, {id: 4}]

cache.changeItem({id: 3, log: 'some data'}); // Изменяем объект в кэше
cache.getData() // [{id: 2}, {id: 3, log: 'some data'}, {id: 4}]

cache.setCacheChunk([{id: 5}, {id: 6}]); // Добавляем несколько объектов в заполненный кэш
cache.getData() // [{id: 3, log: 'some data'}, {id: 4}, {id: 5}, {id: 6}]

cache.setCacheChunk({id: 3, field: 'some value'}); // Измененный объект перестает быть таким
// Из-за того что объект был установлен снова, его приоритет повышен
cache.getData() // [{id: 5}, {id: 6}, {id: 3, field: 'some value}]

cache.setCacheChunk([{id: 7}, {id: 8}, {id: 9}]); // Добавляем объекты в кэш
cache.getCacheItemById(7); //Читаем объекты из кэша
cache.getCacheItemById(8);
cache.getData() // [{id: 9}, {id: 7}, {id: 8}]
На что следует обратить внимание:

Размер кэша (без измененных данных) должен быть не больше maxSize;
При вызове функции получения данных getCacheItemById, приоритет полученного элемента кэша повышается над остальными;
Добавленные элементы через setCacheChunk так же получают повышенный приоритет над остальными в порядке добавления;
Измененные пользователем данные должны оставаться в кэше;
Измененные пользователем данные не учитываются в подсчете размера кэша;
При получении с сервера новой версии измененных данных (совпадают по id) они перестают быть измененными и новая версия данных кэшируется по основным правилам.
Для корректной проверки решения, при отправке выбирайте (make) компилятор.
*/

module.exports = function getCache(maxSize) {
    let cache = [];
    const changedItems = new Map();

    function updateCacheOrder(item) {
        const index = cache.findIndex(cachedItem => cachedItem.id === item.id);
        if (index > -1) {
            cache.splice(index, 1);
        }
        cache.push(item);
        if (cache.length > maxSize) {
            cache.shift();
        }
    }

    return {
        setCacheChunk: (value) => {
            const items = Array.isArray(value) ? value : [value];
            items.forEach(item => {
                const changedItem = changedItems.get(item.id);
                if (changedItem) {
                    item = changedItem;
                    changedItems.delete(item.id);
                }
                updateCacheOrder(item);
            });
        },
        changeItem: (newData) => {
            const items = Array.isArray(newData) ? newData : [newData];
            items.forEach(newItem => {
                const existingItem = cache.find(cachedItem => cachedItem.id === newItem.id);
                if (existingItem) {
                    const newItemWithChanges = { ...existingItem, ...newItem };
                    changedItems.set(newItem.id, newItemWithChanges);
                    updateCacheOrder(newItemWithChanges);
                }
            });
        },
        getCacheItemById: (id) => {
            let item = cache.find(cachedItem => cachedItem.id === id);
            if (item) {
                updateCacheOrder(item);
                return item;
            }
            const changedItem = changedItems.get(id);
            if (changedItem) {
                return changedItem;
            }
            return undefined;
        },
        getData: () => {
            const data = [...cache];
            changedItems.forEach(item => {
                const index = data.findIndex(cachedItem => cachedItem.id === item.id);
                if (index > -1) {
                    data[index] = item;
                } else {
                    data.push(item);
                }
            });
            return data;
        }
    };
};