/*A. Поиск коллеги
Сегодня мы станем частью большой и очень значительной транснациональной корпорации Yandex Contest 2024. В ней работает много сотрудников и, как часто это бывает, нельзя просто так взять и найти нужный контакт человека из соседней команды, соседней группы, соседнего бизнес-юнита. Иной раз требуется обойти большую цепочку коллег для того, чтобы получить необходимый контакт. Требуется написать программу, которая поможет нашим коллегам находить самый короткий путь от них до желаемого контакта.

graph — объект ключ/значение. Количество ключей 0 ≤ N ≤ 50, количество значений 0 ≤ N ≤ 50
startVertex — начальная вершина
endVertex — конечная вершина
Шаблон
/**
 * @param {{
 *  graph: Record<string, string[]>,
 *  startVertex: string,
 *  endVertex: string,
 * }}
 * @returns {string[]}
 */
/*
module.exports = function solution({ graph, startVertex, endVertex }) {
    // ваш код
}
Формат ввода
Пример 1
module.exports = {
  graph: {
    Александра: ["Борис"],
    Борис: ["Александра", "Светлана"],
    Светлана: ["Борис"],
  },
  startVertex: "Александра",
  endVertex: "Светлана",
};
Пример 2
module.exports = {
  graph: {
    Артемий: ["Бронислав", "Дементий"],
    Бронислав: ["Артемий", "Софья", "Дементий"],
    Софья: ["Бронислав"],
    Дементий: ["Артемий","Бронислав"],
    Фаина: ["Гаврила"],
    Гаврила: ["Фаина"],
  },
  startVertex: "Артемий",
  endVertex: "Фаина",
};
Формат вывода
Пример 1
Самый короткий путь от Александры до Светланы

["Александра", "Борис", "Светлана"]
Пример 2
Путь от Артемия до Фаины отсутствует, поэтому выводим пустой массив

[]
*/

/**
 * @param {{
*  graph: Record<string, string[]>,
*  startVertex: string,
*  endVertex: string,
* }}
* @returns {string[]}
*/
module.exports = function solution({ graph, startVertex, endVertex }) {
   if (!graph[startVertex] || !graph[endVertex]) {
       return [];
   }
   
   let queue = [[startVertex]];
   let visited = new Set();
   visited.add(startVertex);
   
   while (queue.length > 0) {
       let path = queue.shift();
       let node = path[path.length - 1];
       
       if (node === endVertex) {
           return path;
       }
       
       for (let neighbor of (graph[node] || [])) {
           if (!visited.has(neighbor)) {
               visited.add(neighbor);
               queue.push([...path, neighbor]);
           }
       }
   }
   
   return [];
};
