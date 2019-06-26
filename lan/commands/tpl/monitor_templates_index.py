html = '''
<!DOCTYPE html>
<html lang="zh">
<head>
    <title>服务器监控</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.bootcss.com/twitter-bootstrap/4.0.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdn.bootcss.com/twitter-bootstrap/3.4.1/css/bootstrap-theme.min.css">
    <style>
        body {
            font-family: Molengo, "Hiragino Sans GB", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif;
        }

        .announcement {
            color: #777;
            border-bottom: solid 3px #d0d0d0;
            background-color: #fff;
            padding: 10px 10px;
            text-align: center;
            transition: .3s
        }

        .announcement:hover {
            border-bottom: solid 3px #159e83;
            transition: .3s
        }

        .announcement p {
            display: inline-block;
            font-size: 15px;
            margin: 0;
            line-height: 1;
            text-indent: 5px
        }

        .announcement i {
            display: inline-block;
            font-size: 15px;
            margin: 0;
            line-height: 1;
            color: #444
        }

        .navbar {
            min-height: 50px
        }

        .navbar-top {
            background-color: #4a4a4a !important;
            border-bottom: 6px solid #159e83;
            -moz-box-shadow: 0 -4px 0 rgba(0, 0, 0, .1);
            box-shadow: 0 6px 0 rgba(0, 0, 0, .1)
        }

        .navbar-brand {
            color: #fff;
            padding: 10px;
            font-size: 20px
        }

        .dropdown .dropdown-toggle {
            padding-bottom: 10px;
            padding-top: 10px
        }

        .navbar-inverse .navbar-brand {
            color: #fff;
            padding: 15px 20px 10px;
            font-size: 20px
        }

        .content {
            background: #fff;
            padding: 20px;
            border: 1px #cecece solid;
            -webkit-box-shadow: 0 1px 10px rgba(0, 0, 0, .1);
            -moz-box-shadow: 0 1px 10px rgba(0, 0, 0, .1);
            box-shadow: 0 1px 10px rgba(0, 0, 0, .1);
            margin-bottom: 20px;
            margin-top: 20px
        }

        .table {
            background: #fff;
            margin-bottom: 0;
            border-collapse: collapse;
            border-radius: 3px
        }

        .table th, .table td {
            text-align: center
        }

        .table-striped tbody > tr.even > td, .table-striped tbody > tr.even > th {
            background-color: #f9f9f9
        }

        .table-striped tbody > tr.odd > td, .table-striped tbody > tr.odd > th {
            background-color: #FFF
        }

        .progress {
            margin-bottom: 0
        }

        .progress-bar {
            color: #000
        }

        .table-hover > tbody > tr:hover > td {
            background: #e6e6e6
        }

        tr.even.expandRow > :hover {
            background: #f9f9f9 !important
        }

        tr.odd.expandRow > :hover {
            background: #FFF !important
        }

        .expandRow > td {
            padding: 0 !important;
            border-top: 0 !important
        }

        #cpu, #ram, #hdd, #network, #traffic {
            min-width: 55px;
            max-width: 100px
        }

        @media only screen and (max-width: 992px) {
            #location, tr td:nth-child(4) {
                display: none;
                visibility: hidden
            }
        }

        @media only screen and (max-width: 720px) {
            #type, tr td:nth-child(3) {
                display: none;
                visibility: hidden
            }

            #location, tr td:nth-child(4) {
                display: none;
                visibility: hidden
            }

            #uptime, tr td:nth-child(5) {
                display: none;
                visibility: hidden
            }
        }

        @media only screen and (max-width: 600px) {
            #type, tr td:nth-child(3) {
                display: none;
                visibility: hidden
            }

            #location, tr td:nth-child(4) {
                display: none;
                visibility: hidden
            }

            #uptime, tr td:nth-child(5) {
                display: none;
                visibility: hidden
            }

            #load, tr td:nth-child(6) {
                display: none;
                visibility: hidden
            }
        }

        @media only screen and (max-width: 533px) {
            #type, tr td:nth-child(3) {
                display: none;
                visibility: hidden
            }

            #location, tr td:nth-child(4) {
                display: none;
                visibility: hidden
            }

            #uptime, tr td:nth-child(5) {
                display: none;
                visibility: hidden
            }

            #traffic, tr td:nth-child(8) {
                display: none;
                visibility: hidden
            }

            #load, tr td:nth-child(6) {
                display: none;
                visibility: hidden
            }
        }

        @media only screen and (max-width: 450px) {
            body {
                font-size: 10px
            }

            .content {
                padding: 0
            }

            #name, tr td:nth-child(2) {
                min-width: 20px;
                max-width: 60px;
                text-overflow: ellipsis;
                white-space: nowrap;
                overflow: hidden
            }

            #type, tr td:nth-child(3) {
                display: none;
                visibility: hidden
            }

            #location, tr td:nth-child(4) {
                display: none;
                visibility: hidden
            }

            #uptime, tr td:nth-child(5) {
                display: none;
                visibility: hidden
            }

            #traffic, tr td:nth-child(8) {
                display: none;
                visibility: hidden
            }

            #hdd, tr td:nth-child(11) {
                display: none;
                visibility: hidden
            }

            #cpu, #ram {
                min-width: 20px;
                max-width: 40px
            }
        }

        .navbar-brand {
            color: #fff
        }
    </style>
    <script src="https://cdn.bootcss.com/jquery/1.12.0/jquery.min.js"></script>
</head>
<body>
<div role="navigation" class="navbar navbar-inverse navbar-fixed-top navbar-top">
    <div class="navbar-inner">
        <div class="container">
            <div class="navbar-header">
                <span class="navbar-brand">Lan服务器监控</span>
            </div>
        </div>
    </div>
</div>

<div class="container content">
    <div id="loading-notice">
        <div class="progress progress-striped center-block active">
            <div class="progress-bar progress-bar-warning" style="width: 100%;">加载中...</div>
        </div>
    </div>
    <table class="table table-striped table-condensed table-hover">
        <thead>
        <tr>
            <th id="uptime">在线时间</th>
            <th id="load">负载</th>
            <th id="cpu">CPU</th>
            <th id="ram">内存</th>
            <th id="hdd">硬盘</th>
        </tr>
        </thead>
        <tbody id="servers">

        </tbody>
    </table>
    <br/>
    <div id="updated" style="margin-left: 5px;">更新中...</div>
</div>

<script>
    $(function () {
        //let _port = {{ port }};
        // console.log(_port);
        $.ajax({
            type : "get",
            url : "/get_data",
            success : function(result) {
                console.log(result);
            },
            error : function(e){
                console.log(e.status);
                console.log(e.responseText);
            }
        });
    })

</script>
</body>
</html>
'''


def get_html():
    return html


if __name__ == '__main__':
    print(get_html())
