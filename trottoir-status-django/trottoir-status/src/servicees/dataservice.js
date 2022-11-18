import http from "../http-common";

class DataService {
  getAll() {
    return http.get("/myapp");
  }

  get(id) {
    return http.get(`/myapp/${id}`);
  }

  delete(id) {
    return http.delete(`/myapp/${id}`);
  }

  findByTitle(title) {
    return http.get(`/myapp?title=${title}`);
  }
}

export default new DataService();