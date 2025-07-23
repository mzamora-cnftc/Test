export class User {
    private id: string;
    private name: string;

    constructor(id: string, name: string) {
        this.id = id;
        this.name = name;
    }

    public updateName(newName: string): void {
        this.name = newName;
    }

    public getId(): string {
        return this.id;
    }

    public getName(): string {
        return this.name;
    }
}