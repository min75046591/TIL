Next.js는 강력하고 유연한 React 프레임워크로, 서버 사이드 렌더링(SSR)과 정적 사이트 생성(SSG)을 포함한 다양한 기능을 제공합니다. 다음은 Next.js를 사용하기 위해 꼭 알아야 할 주제들입니다. 각 주제는 Next.js 공식 문서를 참고하여 예시 코드와 함께 자세히 설명합니다.

### 1. **페이지와 라우팅**
Next.js의 페이지는 `pages` 디렉토리에서 자동으로 라우팅됩니다.

#### 예시 코드
`pages/index.js`
```javascript
export default function Home() {
  return <h1>Welcome to Next.js!</h1>;
}
```
`pages/about.js`
```javascript
export default function About() {
  return <h1>About Us</h1>;
}
```

#### 설명
- `pages` 디렉토리에 있는 각 파일은 자동으로 URL 경로와 매핑됩니다. 예를 들어, `pages/about.js`는 `/about` 경로에 매핑됩니다.
- Next.js는 파일 시스템 기반 라우팅을 사용하여 별도의 라우팅 설정 없이도 라우트를 정의할 수 있습니다.

### 2. **동적 라우팅**
동적 라우팅을 사용하면 URL 파라미터를 처리할 수 있습니다.

#### 예시 코드
`pages/posts/[id].js`
```javascript
import { useRouter } from 'next/router';

export default function Post() {
  const router = useRouter();
  const { id } = router.query;

  return <h1>Post: {id}</h1>;
}
```

#### 설명
- 대괄호 `[]`를 사용하여 동적 라우트를 정의합니다. 예를 들어, `pages/posts/[id].js`는 `/posts/1`, `/posts/2` 등의 경로에 매핑됩니다.
- `useRouter` 훅을 사용하여 URL 파라미터에 접근할 수 있습니다.

### 3. **데이터 페칭**
Next.js는 서버 사이드 렌더링(SSR)과 정적 사이트 생성(SSG)을 지원하며, 각각 `getServerSideProps`와 `getStaticProps` 함수를 사용하여 데이터를 페칭합니다.

#### 서버 사이드 렌더링 (SSR)
`pages/index.js`
```javascript
export async function getServerSideProps() {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();

  return {
    props: {
      data,
    },
  };
}

export default function Home({ data }) {
  return <div>{JSON.stringify(data)}</div>;
}
```

#### 정적 사이트 생성 (SSG)
`pages/index.js`
```javascript
export async function getStaticProps() {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();

  return {
    props: {
      data,
    },
    revalidate: 10, // 10초마다 데이터를 재생성
  };
}

export default function Home({ data }) {
  return <div>{JSON.stringify(data)}</div>;
}
```

#### 설명
- `getServerSideProps`는 서버에서 요청이 있을 때마다 호출되며, 매번 새로운 데이터를 가져옵니다.
- `getStaticProps`는 빌드 시 한 번 호출되며, 정적 페이지를 생성합니다. `revalidate` 옵션을 사용하여 지정된 시간마다 페이지를 재생성할 수 있습니다.

### 4. **API 라우트**
Next.js는 API 라우트를 제공하여 서버리스 함수를 쉽게 만들 수 있습니다.

#### 예시 코드
`pages/api/hello.js`
```javascript
export default function handler(req, res) {
  res.status(200).json({ message: 'Hello, world!' });
}
```

#### 설명
- `pages/api` 디렉토리에서 파일을 생성하면, 해당 파일이 API 엔드포인트가 됩니다.
- API 엔드포인트는 서버리스 함수로 동작하며, 클라이언트에서 쉽게 호출할 수 있습니다.

### 5. **스타일링**
Next.js는 다양한 스타일링 옵션을 제공합니다. CSS 모듈, 전역 CSS, styled-components 등을 사용할 수 있습니다.

#### CSS 모듈 예시
`styles/Home.module.css`
```css
.container {
  margin: 0 auto;
  padding: 2rem;
  max-width: 800px;
}
```

`pages/index.js`
```javascript
import styles from '../styles/Home.module.css';

export default function Home() {
  return <div className={styles.container}>Welcome to Next.js!</div>;
}
```

#### 설명
- CSS 모듈은 파일 단위로 CSS를 적용할 수 있게 하며, 클래스 이름 충돌을 방지합니다.
- Next.js는 `.module.css` 파일을 자동으로 CSS 모듈로 인식합니다.

### 6. **이미지 최적화**
Next.js는 `next/image` 컴포넌트를 제공하여 이미지 최적화를 쉽게 수행할 수 있습니다.

#### 예시 코드
```javascript
import Image from 'next/image';

export default function Home() {
  return (
    <div>
      <h1>Welcome to Next.js!</h1>
      <Image src="/vercel.svg" alt="Vercel Logo" width={72} height={16} />
    </div>
  );
}
```

#### 설명
- `next/image` 컴포넌트는 자동으로 이미지를 최적화하며, 다양한 이미지 형식을 지원합니다.
- width와 height 속성을 지정하여 이미지 크기를 정의할 수 있습니다.

### 7. **환경 변수**
Next.js는 `.env` 파일을 통해 환경 변수를 관리할 수 있습니다.

#### 예시 코드
`.env.local`
```plaintext
NEXT_PUBLIC_API_URL=https://api.example.com
```

`pages/index.js`
```javascript
export default function Home() {
  const apiUrl = process.env.NEXT_PUBLIC_API_URL;
  return (
    <div>
      <h1>Welcome to Next.js!</h1>
      <p>API URL: {apiUrl}</p>
    </div>
  );
}
```

#### 설명
- `.env.local` 파일에 환경 변수를 정의하고, `process.env`를 통해 접근할 수 있습니다.
- `NEXT_PUBLIC_` 접두어를 사용하면 클라이언트 사이드에서 환경 변수를 사용할 수 있습니다.

### 8. **빌드와 배포**
Next.js 애플리케이션을 빌드하고 배포하는 방법을 알아봅니다.

#### 빌드
```bash
npm run build
```

#### 배포
Vercel을 사용한 배포 예시:
```bash
npm install -g vercel
vercel
```

#### 설명
- `npm run build` 명령어는 Next.js 애플리케이션을 프로덕션 환경에 최적화된 상태로 빌드합니다.
- Vercel은 Next.js의 공식 배포 플랫폼으로, 쉽게 배포할 수 있습니다.

### 9. **커스텀 서버**
Next.js는 커스텀 서버를 설정할 수 있습니다. 예를 들어, Express.js와 함께 사용할 수 있습니다.

#### 예시 코드
`server.js`
```javascript
const express = require('express');
const next = require('next');

const dev = process.env.NODE_ENV !== 'production';
const app = next({ dev });
const handle = app.getRequestHandler();

app.prepare().then(() => {
  const server = express();

  server.get('/p/:id', (req, res) => {
    const actualPage = '/post';
    const queryParams = { id: req.params.id };
    app.render(req, res, actualPage, queryParams);
  });

  server.all('*', (req, res) => {
    return handle(req, res);
  });

  server.listen(3000, (err) => {
    if (err) throw err;
    console.log('> Ready on http://localhost:3000');
  });
});
```

`package.json`
```json
{
  "scripts": {
    "dev": "node server.js"
  }
}
```

#### 설명
- Next.js 애플리케이션을 Express.js와 함께 실행하여 커스텀 서버를 설정할 수 있습니다.
- 커스텀 서버를 사용하면 라우팅, 미들웨어 등을 자유롭게 설정할 수 있습니다.

### 10. **플러그인과 확장**
Next.js는 다양한 플러그인과 확장 기능을 제공합니다. 예를 들어, TypeScript 설정, Sass 사용 등을 설정할 수 있습니다.

#### TypeScript 설정
```bash
npm install --save-dev typescript @types/react @types/node
```
`tsconfig.json` 파일이 자동으로 생성됩니다.

#### Sass 사용
```bash
npm install sass
```
`styles/globals.scss`
```scss
body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif;
}
```

`pages/_app.js`
```javascript
import '../styles/globals.scss';

function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}

export default MyApp;
```

### 11. **중첩 레이아웃**
Next.js에서 중첩 레이아웃을 구현할 수 있습니다.

#### 예시 코드
`components/Layout.js`
```javascript
export default function

 Layout({ children }) {
  return (
    <div>
      <header>
        <h1>My Next.js App</h1>
      </header>
      <main>{children}</main>
      <footer>
        <p>Footer content here</p>
      </footer>
    </div>
  );
}
```

`pages/_app.js`
```javascript
import Layout from '../components/Layout';
import '../styles/globals.css';

function MyApp({ Component, pageProps }) {
  return (
    <Layout>
      <Component {...pageProps} />
    </Layout>
  );
}

export default MyApp;
```

#### 설명
- `components/Layout.js` 파일을 생성하여 공통 레이아웃을 정의합니다.
- `_app.js` 파일에서 모든 페이지에 이 레이아웃을 적용할 수 있습니다.

### 12. **SEO 최적화**
Next.js는 내장된 `next/head` 컴포넌트를 사용하여 SEO 최적화를 할 수 있습니다.

#### 예시 코드
```javascript
import Head from 'next/head';

export default function Home() {
  return (
    <div>
      <Head>
        <title>My Next.js App</title>
        <meta name="description" content="Welcome to my Next.js app" />
      </Head>
      <h1>Welcome to Next.js!</h1>
    </div>
  );
}
```

#### 설명
- `next/head` 컴포넌트를 사용하여 각 페이지에 메타 태그를 추가할 수 있습니다.
- SEO 최적화를 통해 검색 엔진에서의 가시성을 높일 수 있습니다.

### 13. **커스텀 에러 페이지**
Next.js에서 커스텀 에러 페이지를 구현할 수 있습니다.

#### 예시 코드
`pages/404.js`
```javascript
export default function Custom404() {
  return <h1>404 - Page Not Found</h1>;
}
```

`pages/_error.js`
```javascript
function Error({ statusCode }) {
  return (
    <p>
      {statusCode
        ? `An error ${statusCode} occurred on server`
        : 'An error occurred on client'}
    </p>
  );
}

Error.getInitialProps = ({ res, err }) => {
  const statusCode = res ? res.statusCode : err ? err.statusCode : 404;
  return { statusCode };
};

export default Error;
```

#### 설명
- `pages/404.js` 파일을 생성하여 커스텀 404 페이지를 구현할 수 있습니다.
- `pages/_error.js` 파일을 생성하여 다른 에러 페이지를 커스터마이즈할 수 있습니다.

이렇게 Next.js의 주요 기능과 사용법을 주제별로 나눠서 설명했습니다. 각 기능에 대해 더 자세한 내용을 알고 싶다면 [Next.js 공식 문서](https://nextjs.org/docs)를 참고하면 많은 도움이 될 것입니다. Next.js를 사용하여 프로젝트를 진행하는 데 필요한 모든 기본 사항들을 포함하여 설명드렸습니다.