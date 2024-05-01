chrome.action.onClicked.addListener(async () => {

    // 左端を残して全てのタブを消す
    async function deleting(pages) {
        const len = pages.length - 1;
        for (let i = len; i > 0; i--) {
            await chrome.tabs.remove(pages[i].id);
        }
    }

    // エラー起きてたらメッセージ出力
    function onError(error) {
        console.log(`エラーメッセージ： ${error}`);
    }

    // currentWindow：アクティブウィンドウ上のみ実行
    const queries = chrome.tabs.query({ currentWindow: true });
    queries.then(deleting, onError);
});
