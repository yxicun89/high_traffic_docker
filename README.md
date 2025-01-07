# 負荷分散

このプロジェクトは、特にゲームおよびビデオストリーミングアプリケーションに焦点を当てた、高トラフィックサービス向けのスケーラブルでロードバランスされたバックエンドソリューションを提供することを目的としています。

## プロジェクト構成

- **gaming/**: モデル、ビュー、およびURLルーティングを含むゲームアプリケーション。
- **video_streaming/**: モデル、ビュー、およびURLルーティングを含むビデオストリーミングアプリケーション。
- **load_balancer/**: 複数のサーバーにトラフィックを分散するためのロードバランシングロジックを実装。
- **high_traffic_backend/**: 設定および構成を含むメインのDjangoプロジェクトディレクトリ。
- **manage.py**: Djangoプロジェクトと対話するためのコマンドラインユーティリティ。
- **requirements.txt**: プロジェクトに必要な依存関係をリスト。

## 特徴

- 効率的なトラフィック分散のためのロードバランシング。
- 高トラフィックを処理するためのスケーラブルなアーキテクチャ。
- ゲームおよびビデオストリーミングのためのモジュラーアプリケーション。

## インストール

1. リポジトリをクローンします。
    ```sh
    git clone <リポジトリのURL>
    ```
2. プロジェクトディレクトリに移動します。
    ```sh
    cd high_traffic
    ```
3. Dockerを使用して環境を構築します。
    ```sh
    docker-compose -f docker/docker-compose.yaml up --build
    ```
4. データベースマイグレーションを実行します。
    ```sh
    docker-compose -f docker/docker-compose.yaml exec web python manage.py migrate
    ```
5. lucastでロードバランシングテストを行います。
   ```sh
   docker-compose -f docker/docker-compose.yaml exec web python run_locust_tests.py
   ```

これで、Dockerを使用してDjango環境が構築され、負荷分散のテストを行えます！