<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Paizanalizer</title>
    <link rel="stylesheet" href="/static/css/bulma.min.css">
</head>
<body>
    <section class="section">
        <form action="/" method="post">
            <div class="container">
                <h1 class='title is-1'>Paizanalizer</h1>
                <div class="field">
                    <div class="control">
                        <input class="input" type="text" name='mail' placeholder="Mail Address..." required>
                    </div>
                </div>
                <div class="field">
                    <div class="control">
                        <input class="input" type="password" name='pass' placeholder="Password..." required>
                    </div>
                </div>
                <div class="field is-grouped">
                    <div class="control">
                        <input class="button is-link" id='button' type="submit" value="Submit">
                    </div>
                </div>
            </div>
        </form>
    </section>

    <section class="section">
        <div class="container">
            <h3 class='title is-3'>Results</h3>
            <div id="result">
                <input class="search input" placeholder="Search..." />
                <table class="table is-hoverable">
                    <thead>
                        <tr>
                            <th class='sort' data-sort='no'>No.</th>
                            <th class='sort' data-sort='ttl'>Title</th>
                            <th class='sort' data-sort='times'>Times</th>
                            <th class='sort' data-sort='details'>Details</th>
                        </tr>
                    </thead>
                    <tbody class='list'>
                        {% for key in data %}
                        <tr>
                            <td class='no'>{{ key }}</td>
                            <td class='ttl'>{{ data[key][0] }}</td>
                            <td class='times'>{{ data[key][1] | length }}</td>                     
                            <td class='details' style='display:flex; flex-wrap:wrap;'>
                                {% for card in data[key][1] %}
                                <div class="card" style='margin-right:4px; margin-bottom:4px'>
                                <div style='margin:4px'>
                                    <p><b>{{ card[0] }}</b></p>
                                    <p>{{ card[2] }}</p>
                                    <p >{{ card[1] }}</p>
                                </div>
                                </div>
                                {% endfor %} 
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </section>
<script src="//cdnjs.cloudflare.com/ajax/libs/list.js/1.5.0/list.min.js"></script>

<script>
    let options = {
        valueNames: ['no', 'ttl', 'times', 'details']
    };
    let userList = new List('result', options);
</script>

</body>
</html>