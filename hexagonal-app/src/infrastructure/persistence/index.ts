import { UserRepository } from '../../domain/repositories';
import { User } from '../../domain/entities';

export class UserRepositoryImpl implements UserRepository {
    private users: User[] = [];

    async findById(id: string): Promise<User | null> {
        return this.users.find(user => user.id === id) || null;
    }

    async save(user: User): Promise<void> {
        this.users.push(user);
    }
}