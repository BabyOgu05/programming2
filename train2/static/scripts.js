const url = '/';  // 프록시 서버 URL

fetch(url)
    .then(response => response.json())
    .then(data => {
        console.log(data);  // API 응답을 출력합니다.
        const newsContainer = document.getElementById('news');
        data.items.forEach(item => {
            const articleElement = document.createElement('div');
            articleElement.classList.add('news-item');
            articleElement.innerHTML = `
                <div class="news-header">
                    
                    <span class="source">${item.source}</span>
                    <span class="time">${item.pubDate}</span>
                </div>
                <h2><a href="${item.link}" target="_blank">${item.title}</a></h2>
                <div class="news-body">
                    <p>${item.description}</p>
                    <p class="source-text">출처: ${item.source}</p>
                </div>
            `;
            newsContainer.appendChild(articleElement);
        });
    })
    .catch(error => console.error('Error:', error));
