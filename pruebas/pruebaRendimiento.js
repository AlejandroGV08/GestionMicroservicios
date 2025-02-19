import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    vus: 10, // 10 usuarios virtuales
    duration: '30s', // Duración de la prueba
};

export default function () {
    const url = 'http://192.168.1.35:5000/usuarios';
    const payload = JSON.stringify({
        id: __ITER,
        nombre: `Usuario ${__ITER}`,
        email: `usuario${__ITER}@example.com`
    });s

    const params = {
        headers: { 'Content-Type': 'application/json' },
    };

    const res = http.post(url, payload, params);
    check(res, {
        'status is 201': (r) => r.status === 201,
    });
    sleep(1);
}